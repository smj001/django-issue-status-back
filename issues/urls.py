from django.urls import path
from .views import LatestIssueListAPIView

app_name = 'issues'

urlpatterns = [
    path('latest/', LatestIssueListAPIView.as_view(), name='latest_issues'),
]
