# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import AskForm, AnswerForm, NewUserForm, LoginForm

from django.contrib.auth.decorators import login_required
import logging


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def index(request, *args, **kwargs):

	return render(request, 'question/index.html', {'questions': paginate(request, Question.objects.resent_questions()),})

@require_GET
def popular(request, *args, **kwargs):
	return render(request, 'question/index.html', {'questions': paginate(request, Question.objects.popular_questions()),})


@require_GET
def question_details(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	form = AnswerForm(initial = {'question': question_id})
	
	return render(request, 'question/details.html', {'question': question, 'form': form})

# @login_required
def question_add(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		import pdb; pdb.set_trace()
		form.instance.author = request.user
		if form.is_valid():
			question = form.save()
			url = question.get_absolute_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'question/add.html', {'form' : form})

def signup(request):
	if request.method == 'POST':
		logger = logging.getLogger(__name__)
		form = NewUserForm(request.POST)
		logger.error(str(form))
		if form.is_valid():
			user = form.save()
			user = authenticate(username=user.username, password=form.cleaned_data['password'])
			if user is not None:
				# залогинить нового пользователя
				login(request, user)
				# отправить нового пользователя на главную страницу
				return HttpResponseRedirect('/')
	else:
		form = NewUserForm()
	return render(request, 'user/signup.html', {'form' : form})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					# отправить пользователя на главную страницу
					return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'user/login.html', {'form' : form})


# @login_required
def answer_add(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		form.instance.author = request.user
		if form.is_valid():
			answer = form.save()
			url = answer.question.get_absolute_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm()
	return render(request, 'answer/add.html', {'form' : form})

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 10:
		limit = 10
	try:
		page = int(request.GET.get('page',1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page
