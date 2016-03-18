# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Question, Answer

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса
class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

	# def __init__(self, user, **kwargs):
	# 	self._user = user
	# 	super(AskForm, self).__init__(**kwargs)

	def clean(self):
		return super(AskForm, self).clean()


	def save(self):
		# self.cleaned_data['author'] = self._user
		question = Question(**self.cleaned_data)

		question.save()
		return question


# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом
class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']

	def clean(self):
		return super(AnswerForm, self).clean()


	def save(self):
		# self.cleaned_data['author'] = self._user
		answer = Answer(**self.cleaned_data)

		answer.save()
		return answer