# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name='question_user')
	likes = models.ManyToManyField(User, related_name='%(app_label)s_%(class)s_related', null=True)

# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question =  models.ForeignKey(Question)
	author = models.ForeignKey(User)