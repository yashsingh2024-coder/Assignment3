from django.urls import path
from teaching_staff import views

urlpatterns = [
    path("",views.teaching_staff_home),
    path("profile/",views.teaching_staff_profile),
]