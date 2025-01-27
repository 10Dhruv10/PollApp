from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
#in admin page the object will have same name as title
#also when i directly use {{ Task_object }} in template it will show title only
    