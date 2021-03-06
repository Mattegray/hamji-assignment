import requests
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets
from itertools import chain

from utils.url import restify

from .models import Choice, Question, Comment
from .serializers import QuestionSerializer

from .forms import CommentForm, ChoiceForm


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        response = requests.get(restify("/questions/"))
        temp = response.json()
        questions = []
        for question in temp:
            if not question['closed']:
                questions.append(question)
        questions.sort(key=lambda x: x['pub_date'], reverse=True)
        return questions[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # List of active comments for this post
    comments = question.comments.all()
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
                    ###
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current question to the comment
            new_comment.question = question
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    else:
        comment_form = CommentForm()
    return render(request,
                  'polls/detail.html',
                  {'question': question,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    new_choice = None
    if request.method == 'POST':
        # A comment was posted
        choice_form = ChoiceForm(data=request.POST)
        if choice_form.is_valid():
            # Create Comment object but don't save to database yet
            new_choice = choice_form.save(commit=False)
            # Assign the current question to the comment
            new_choice.question = question
            # Save the comment to the database
            try:
                new_choice.save()
            except ValueError:
                return render(
                    request,
                    "polls/detail.html",
                    {
                        "question": question,
                        "error_message": "There are already more than 5 choices.",
                    },
                )

            return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    else:
        choice_form = ChoiceForm()
    return render(request,
                  'polls/detail.html',
                  {'question': question,
                   'new_choice': new_choice,
                   'choice_form': choice_form})


class SearchResultsView(generic.ListView):
    model = Question, Choice
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        questions = Question.objects.filter(
            Q(question_text__icontains=query)
        )
        choices = Choice.objects.filter(
            Q(choice_text__icontains=query)
        )
        object_list = chain(questions, choices)
        return object_list

# API
# ===


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
