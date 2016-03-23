# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import Question, Answer
from django.contrib.auth.models import User

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса
class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

	def clean(self):
		return super(AskForm, self).clean()


	def save(self):
		question = Question(**self.cleaned_data)
		question.author = self.instance.author

		question.save()
		return question


# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом
class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']
		widgets = {'question': forms.HiddenInput()}

	def clean(self):
		return super(AnswerForm, self).clean()


	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.author = self.instance.author

		answer.save()
		return answer

# username - имя пользователя, логин
# email - email пользователя
# password - пароль пользователя
class NewUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		widgets = { 'password': forms.PasswordInput(),}

	def clean(self):
		return super(NewUserForm, self).clean()

	def save(self):
		user = User.objects.create_user(**self.cleaned_data)

		user.save()
		return user

# username - имя пользователя, логин
# password - пароль пользователя
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	# class Meta:
	# 	model = User
	# 	fields = ['username', 'password']
	# 	widgets = { 'password': forms.PasswordInput(),}

	def clean(self):
		return super(LoginForm, self).clean()

	def save(self):
		pass