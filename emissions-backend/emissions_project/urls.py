from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from emissions_project.infrastructure.views import EmissionListView

def home(request):
    return HttpResponse("Backend is running!")

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/emissions/", EmissionListView.as_view(), name="emission-list"),
]
