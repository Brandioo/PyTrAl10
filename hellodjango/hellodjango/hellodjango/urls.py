from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profiles/", views.get_profile_list, name="profile-list"),
    path("profiles/<username>/", views.get_profile, name="profile-details"),
    path("add/<int:x>/<int:y>/", views.add, name="add"),
    path("family-members/<int:emp_id>/", views.get_employee_details, name="employee-details"),
]
