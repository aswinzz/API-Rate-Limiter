from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/1',views.ApiFirst.as_view(),name="ApiFirst"),
    url(r'^api/2',views.ApiSecond.as_view(),name="ApiSecond"),
]