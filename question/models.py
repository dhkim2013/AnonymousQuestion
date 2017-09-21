# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    isAnswered = models.IntegerField(default=0)
    answer = models.TextField()

    def __str__(self):
        return self.question