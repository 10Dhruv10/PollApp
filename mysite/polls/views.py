from django.http import HttpResponse;
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_entries_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_entries_list" : latest_entries_list }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)   #take object of pk from Question
    context = {"q" : q}
    return render(request, "polls/detail.html", context)
    # question = Question.objects.get(pk=question.id)
    # return HttpResponse("Your are viewing details of %s" % question_id)

def results(request, question_id):                #question_id comes from urls.py
    return HttpResponse("You are viewing results of %s" % question_id)

def vote(request, question_id):
    temp = "You are viewing votes for %s"
    return HttpResponse(temp % question_id)
    
    
#request is an instance (object in java) of HttpRequest
#it can be named anything

#when a user visits a page the browser makes an HTTP request.
#After server processes that req, it sends back an HTTP response to the client.

#Query set is collection of rows Objects, its like a list.
#render is to return html templates, 

""" 
    the request in render is get here and renders index.html
    return render(request, "polls/index.html", context)
    
"""

#list_entries_list and q are actually objects of Question model i.e.
#queryset (collection of objects) and a single object
