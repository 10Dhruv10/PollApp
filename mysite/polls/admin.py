from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
#This tell django to add Question to admin panel 

class ChoiceInline(admin.TabularInline):              #inline let us manage records of child(Choice) on parents side(Question)
    model = Choice
    extra = 4                                         #No of times i want to see choice
    
    
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]          #i want to see these 2 only
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date Info", {"fields":["pub_date"], "classes":["collapse"]}),   #"classes":["collapse"] shows a hide and show button for pub_date
    ]
    
    inlines = [ChoiceInline]
    
    list_display = ["question_text", "pub_date", "decorator_method_only"]
    list_filter = ["pub_date"]                                            #add a small filter menu on right side, if the field is weird like text it will only show texts and not have its own logic like in case of date
    search_fields = ["question_text", "pub_date"]                         #add a searching bar, indivually or by both (try <hi 2024>)       #'like' query of sql

admin.site.register(Question, QuestionAdmin)
#(model_name, adminclass_name)
# admin.site.register(Choice)

#now i see a issue when i use the above line, i need to go to choices to add choice, but i want to directly add choices when i am at question, so we will use inline for that
#another issue is am only seeing question_text of various questions when i click Question of polls but want to see more details so use a list for that

#i want to sort by pub_date in Question so lets do that in models.py by using admin decorator