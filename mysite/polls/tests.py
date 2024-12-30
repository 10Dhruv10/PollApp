from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

class QuestionModelTests(TestCase):
    
    def test_future_question_test(self):
        published = timezone.now() + datetime.timedelta(days=30)
        q = Question(pub_date = published)
        
        self.assertIs(q.was_published_recently(), False)
        
        
#Problem - when we add some future poll, 
#          it is being cosnidered as recent which shouldnt be happening
#test function should always begin from test_
#self.assertIs checks if result of q.was_published_recently() is False,
#lets fix our models was_published_recently() function

    def test_past_questions(self):
        published = timezone.now() - datetime.timedelta(days=1, seconds=1)
        q = Question(pub_date = published)
        
        self.assertIs(q.was_published_recently(), False)
    
    def test_recent_questions(self):
        published = timezone.now() - datetime.timedelta(hours = 23, minutes=59, seconds=59)
        q = Question(pub_date = published)
        
        self.assertIs(q.was_published_recently(), True)

#tests designed to deal with all 3 time possibilities


'''

>>> from django.test.utils import setup_test_environment
>>> from django.test import Client
>>> from django.urls import reverse

>>> setup_test_environment()

>>> client = Client() 

>>> response = client.get("/")
        Not Found: /
>>> response = client.get("polls/") 
        Not Found: /polls
        
>>> response = client.get("/polls") 
>>> response.status_code
        301
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
        200
>>> response = client.get("/polls/")
>>> response.status_code
        200
        
>>> response.context["latest_entries_list"]
        <QuerySet [<Question: Yo Man>, <Question: Sup>, <Question: hi>]>      
>>> response.content
        b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
'''

#200 means all good
#404 is error
#301 means url lacks a trailing slash in .get() and it adds one itself and check if that link exixts, if it foes 301 is returned else Not Found: