# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from question.models import Question


class User(AbstractUser):
    questions = models.ManyToManyField(Question)