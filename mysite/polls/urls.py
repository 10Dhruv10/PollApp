#only our project has urls.py, for apps inside it we create a urls.py separately

from django.urls import path;
from . import views;

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

#path function maps URL (e.g., /polls/) to view function (e.g., views.index).
#from . means to import from current directory that is poll 
#to refer url in template we use 'name'


#index.html url visit logic explained ->
#User visits a page say "polls/34"
#Django loads mysite.urls module from ROOT_URLCONF in settings
#Django sees polls/ in urls.py of mysite, Django goes to polls/urls (mysite->polls)
#Django strips off polls/, and sends 34 to polls.urls URLCONF       (polls folder)
#Django matches 34 with <int:question_id>, Detail funtion is called
#<int:question_id> catches the URL part question_id as integer, if user gives 34.0 then 404 error

#Function parameters are captured from urls "<type:smth>"


#app_name ="polls" added to avoid same name url of different application in same project issue
#polls and polls2 both have name="detail" and i want to use detail of polls as of now
#in details.html I can write 'polls:detail' 

#we can refer to links like "polls/question_id/results" as "polls:results question_id" i.e. (app_name: name of url)