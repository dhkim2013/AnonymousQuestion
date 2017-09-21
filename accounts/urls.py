from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^register/$', views.Register.as_view()),
]