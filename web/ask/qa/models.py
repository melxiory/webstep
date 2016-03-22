# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def resent_questions(self):
		return self.order_by('-added_at')

	def popular_questions(self):
		return self.order_by('-rating')

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
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=1)
	author = models.ForeignKey(User, related_name='question_user', blank=True, null=True)
	rating = models.BigIntegerField(default=1)
	likes = models.ManyToManyField(User, related_name='%(app_label)s_%(class)s_related', blank=True)

	objects = QuestionManager()

	@models.permalink
	def get_absolute_url(self):
		return ('qa.views.question_details', [str(self.id)])


# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question =  models.ForeignKey(Question)
	author = models.ForeignKey(User, blank=True, null=True)
