from rest_framework import viewsets, mixins

from api.serializers import FeedbackSerializer
from feedback.models import Feedback

class FeedbackViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    http_method_names = ['get', 'post']

    # def get_serializer_class(self):
    #     """Разделить сериализаторы GET и POST запросов."""
    #     if self.action in ['list', 'retrieve']:
    #         return FeedbackDetailSerializer
    #     return FeedbackSerializer
