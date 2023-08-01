from django.urls import path
from . import views


urlpatterns = [
    path("", views.init_playground),
    path("form/", views.submit_form, name="submit_form"),
    # path("django_form/", views.django_form, name="django_form"),
    # path("django_form/", views.student_form, name="django_form"),
    path("django_form/", views.validate_pass, name="django_form"),
]
