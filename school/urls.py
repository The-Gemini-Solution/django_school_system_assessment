from django.urls import path

from school import views

urlpatterns = [path("classes/<int:class_pk>", views.view_class, name="view_class")]
