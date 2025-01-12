#python manage.py migrate, this creates any necessary database table for INSTALLED_APPS
#Django follows DRY (Dont-Repeat-Yourself) Principle, define model at one place & derive from it
from django.db import models
from django.utils import timezone
import datetime                          #imports from python directly
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data has been Published Blud")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) #return true if published within 24 hours
    
    
    @admin.display(ordering = pub_date, description="Published in 24hour?",)
    def decorator_method_only(self):                                         #we will need to add this to list_display of QuestionAdmin
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  #check if its before or after 24 hours from now
    
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)      #9    
    choice_text = models.CharField(max_length = 100)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text
    
    
#PART 1  :- 

# models is a module, Model makes the fucntions a MODEL in SQLite
# hence Question and Choice are MODELS and not just a function
# question, pub size etc are FIELDS  (COLUMNS in DataBase)

# ForeignKey is used for One(question)-To-Many(choices) Relation
# on_delete = models.CASCADE deletes all the choices(CHILD) of question_id(PARENT)
# when parent is deleted.

# when Django create a column question, it will end with _id & will be question_id
# hence it is conventional to just use name same as (Model's Name) i.e. question 



#PART 2  :-
#  To makemigrations use python manage.py makemigrations polls



#PART 3  :-
#  when creating object of model use keyword argument
#  E.G.  q =  Question(question_text = "", pub_date = ??)

#  Question.objects.all() -> #QuerySet [<Question: Question object (1)>]>
#  is thrown when we have no str function to return fields in human-readable form

#  Question.objects.filter(id=1) -> <QuerySet [<Question: Sup>]>
#  Question.objects.get(id=1)  ->  <Question: Sup>   
#    Filter gives all result matching, Get gives only one, else exception raised
#  Question.objects.get(pk=1)  ->  <Question: Sup>    
#    pk = id when we dont specify one & django create pk field called id in model automatically


'''
>>> q = Question(question_text = "Yo Man", pub_date = timezone.now())
>>>     q.save()
>>> choice1 = Choice(question = q, choice_text = "Doing Fine", votes = 0)
>>>     choice1.save()
>>> choice2 = Choice(question = q, choice_text = "Aight", votes = 1)
>>>     choice2.save()

>>> q = Question.objects.get(id=1)
>>> q.choice_set.all()
        <QuerySet []>
>>> q = Question.objects.get(id=2) 
>>> q.choice_set.all()
        <QuerySet [<Choice: Doing Fine>, <Choice: Aight>]>
        
>>> q.choice_set.count()
        2
>>> q, choice1
    (<Question: Yo Man>, <Choice: Doing Fine>)
    
Choice.objects.all() can also be used but gives all choices in DB,
q.choice_set.all() gives for id that q belongs to
'''