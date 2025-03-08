from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("<slug:video_id>", views.content, name="content"),
]
