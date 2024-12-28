from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

class QuestionModelTests(TestCase):
    def test_future_question_test(self):
        published = timezone.now() + datetime.timedelta(days=30)
        q = Question(pub_date = published)
        
        self.assertIs(q.was_published_recently(), False)
        
#test function should always begin from test_
#this code checks if result of q.was_published_recently() is False,
#as our code doesnt handle future posts correctly, its taking in future polls
#and considering them as recently published and giving true which shouldnt happen.

#lets fix our models was_published_recently() function