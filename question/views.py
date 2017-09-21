# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User
from question.models import Question


class Index(View):
    def get(self, request):
        return render(request, 'question/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class QuestionAndAnswer(View):
    def get(self, request, username):
        return HttpResponse(status=200)

    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse(status=404)
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        questionPK = request.POST.get('questionPK')

        if question is not None:
            q = Question.objects.create(question=question)
            q.save()
            user.questions.add(q)
            user.save()
            return HttpResponse(status=200)
        elif answer is not None and questionPK is not None:
            if request.user.username == username:
                try:
                    user.questions.get(pk=questionPK)
                    q = Question.objects.get(pk=questionPK)
                    q.answer = answer
                    q.isAnswered = 1
                    q.save()
                    return HttpResponse(status=200)
                except:
                    return HttpResponse(status=404)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)