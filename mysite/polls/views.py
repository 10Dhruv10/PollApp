from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.db.models import F
from django.urls import reverse
from django.utils import timezone


def index(request):
    # latest_entries_list = Question.objects.order_by("-pub_date")[:5]    #it has all __str__() results i.e. question_text 
    latest_entries_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]    #__lte is Less Than or Equal to
    context = { "latest_entries_list" : latest_entries_list }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)   #take object of pk from Question
    context = {"q" : q}
    return render(request, "polls/detail.html", context)
    # question = Question.objects.get(pk=question.id)
    # return HttpResponse("Your are viewing details of %s" % question_id)

def results(request, question_id):                #question_id comes from urls.py
    question = get_object_or_404(Question, pk=question_id)
    context = {"question" : question}
    return render(request, "polls/results.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected = question.choice_set.get(pk=request.POST["my_choice"])
        
    except(KeyError, Choice.DoesNotExist):
        context = {"q":question, "error_message": "You didnt select a choice"}
        return render(request, "polls/detail.html", context)
    
    else:
        selected.votes = F("votes") + 1
        selected.save()
        
        return HttpResponseRedirect( reverse ("polls:results", args=(question_id,)) )     #args is a tuple
        
    
    
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

#F is used to perform calculation in DB which is faster
#Key error -> no such id exists, Choice.DoesNotExist -> id exists but no choice, user alter id of existing choices using insepct element

"""
Suppose we change our results in urls.py and make it polls/smth/question_id/results then we will
need to update everywhere we are referencing results in our code if it is like poll/question_id/results
but using reverse we can avoid this and will only need to make change in urls.py

HttpResponseRedirect with reverse does same as {% url 'polls:results' question_id %}
one is used for making a redirecting url for html files and other for views.py

After dealing with post data its a good practice to send user to other page as keeping them on 
same page possess a risk because if they resubmit it or click back button this would lead to extra 
addition of votes so we use "HttpResponseRedirect"
       
"""