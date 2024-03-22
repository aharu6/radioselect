from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F
from .models import Question,Choice,Program

def selectradioprojectPage(request):
    return HttpResponse('radioproject select Page')

class ResultsView(generic.DetailView):
    model = Choice
    template_name = "selectradioproject/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"selectradioproject/detail.html",
                      {"question":question,
                       "error_message":"You didn't select a choice"},
                    )
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()
        return HttpResponseRedirect(reverse("selectradioproject:results",args = (question.id,)))
        
class IndexView(generic.ListView):
    template_name = "selectradioproject/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "selectradioproject/detail.html"

