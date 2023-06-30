from django.urls import path, include
from . import views

urlpatterns = [
    path('task', views.TaskAPIView.as_view()),
    path('relations', views.RelationAPIView.as_view())
]