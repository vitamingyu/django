from django.urls import path
from pro21app import views

urlpatterns = [
    path("survey", views.surveyView),
    path("surveyprocess", views.surveyProcess),
    path("surveyshow", views.surveyAnalysis),
]