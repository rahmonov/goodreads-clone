from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from books.models import BookReview
from api.serializers import BookReviewSerializer


class BookReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'
