from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import Question


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
	
	return render(request, 'question/details.html', {'question': question,})

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