from django.urls import path
from . import views

app_name = "polls"
# '-upn' stands for url pattern name
urlpatterns = [
    path("", views.IndexView.as_view(), name="index-upn"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail-upn"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results-upn"),
    path("<int:question_id>/vote/", views.vote, name="vote-upn")
]
