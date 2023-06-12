from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer

class LatestIssueListAPIView(generics.ListAPIView):
    queryset = Issue.objects.all().order_by('-submit_date')[:20]
    serializer_class = IssueSerializer
