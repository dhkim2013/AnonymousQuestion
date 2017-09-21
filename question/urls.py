from django.conf.urls import url

from question import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^(?P<username>[a-zA-Z0-9]+)/$', views.QuestionAndAnswer.as_view()),
]