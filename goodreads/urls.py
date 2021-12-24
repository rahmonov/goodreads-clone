from django.contrib import admin
from django.urls import path, include

from .views import landing_page


urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("users/", include("users.urls"), name="users"),

    path('admin/', admin.site.urls),
]
