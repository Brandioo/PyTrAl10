from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("about/", views.about),
    path("profiles/", views.get_profile_list),
    path("profiles/<username>/", views.get_profile),
    path("add/<int:x>/<int:y>/", views.add),
]
