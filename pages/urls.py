from django.urls import path
from .views import home, enquiries_api

app_name = "pages"
urlpatterns = [
    path("", home, name="home"),
    path("api/enquiries/", enquiries_api, name="enquiries_api"),
]
