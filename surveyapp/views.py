from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, QuestionChoice, QuestionGuestResponse

import random

def index(request):
  success_message = None
  error_message = None

  if not request.session.session_key:
    request.session.save()

  form_question = request.POST.get("question")
  form_choice = request.POST.get("choice")

  if(form_question != None and form_choice != None):
    form_question_obj = Question.objects.get(pk=form_question)
    form_choice_obj = QuestionChoice.objects.get(pk=form_choice)

    new_response = QuestionGuestResponse.objects.create(
        guest=request.session.session_key,
        question=form_question_obj,
        choice=form_choice_obj
      )

    success_message = "Your response has been recorded!"
  elif(form_question != None and form_choice == None):
    error_message = "You did not select an answer for the previous question."

  # only show questions the current guest hasn't answered
  cur_guest_responses = QuestionGuestResponse.objects.filter(guest=request.session.session_key)
  answered_questions = [response.question.id for response in cur_guest_responses]

  # only select questions with at least one choice (although two might be a little less authoritarian...)
  question_choices = QuestionChoice.objects.values('question').distinct()

  questions = Question.objects \
    .exclude(id__in=answered_questions) \
    .filter(id__in=question_choices)

  random_question = None

  if questions:
    random_question = random.choice(questions)

  # get the choices for the selected question
  choices = QuestionChoice.objects.filter(question=random_question)

  return render(request, 'surveyapp/index.html', {
      'question': random_question,
      'choices': choices,
      'success_message': success_message,
      'error_message': error_message
    })
