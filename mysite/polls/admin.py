from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)

#This tell django to add Question to admin panel 