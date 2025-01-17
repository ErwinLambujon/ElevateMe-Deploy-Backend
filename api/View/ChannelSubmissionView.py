from pydantic import ValidationError
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from api.Model.ChannelSubmission import ChannelSubmission
from api.Model.RoomChannel import RoomChannel
from api.Serializer.ChannelSubmissionSerializer import ChannelSubmissionSerializer
import logging



class ChannelSubmissionView(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = ChannelSubmissionSerializer
    queryset = ChannelSubmission.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChannelSubmission.objects.filter(channel_id=self.kwargs['channel_pk'])

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def submit(self, request, channel_pk=None):
        try:
            channel = RoomChannel.objects.get(id=channel_pk)
        except RoomChannel.DoesNotExist:
            return Response(
                {"error": f"Channel with id {channel_pk} does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        submitted_work = request.FILES.get('submitted_work')
        problem_statement = request.data.get('problem_statement')
        user_submitted = request.user

        serializer = self.get_serializer(data={
            "submitted_work": submitted_work,
            "member_id": user_submitted.id,
            "channel_id": channel.id,
            "problem_statement": problem_statement
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    @action(detail=True, methods=['get'], url_path='download')
    def download_submission(self, request, pk=None, channel_pk=None):
        submission = get_object_or_404(ChannelSubmission, id=pk, channel_id=channel_pk)
        logger = logging.getLogger(__name__)

        if not submission.submitted_work:
            raise Http404("File not found")

        try:
            logger.info(f"Attempting to download file: {submission.submitted_work.name}")
            return FileResponse(
                submission.submitted_work.open('rb'),
                as_attachment=True,
                filename=submission.submitted_work.name
            )
        except FileNotFoundError:
            logger.error("File not found error")
            raise Http404("File not found")