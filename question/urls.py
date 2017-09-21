from django.conf.urls import url

from question import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
]