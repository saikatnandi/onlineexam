from django.contrib import admin

from .models import Mcq_Question
from .models import Topic
from .models import Question_Set




class Mcq_QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'mcq_answer', 'question_set')
    search_fields = ('question_text','choice_a')
    list_filter = ('question_set',)

    
#    fields = ('question_text', 'mcq_answer')
   




# admin.site.register(Mcq_Question, Mcq_QuestionAdmin)
# admin.site.register(Topic)
# admin.site.register(Question_Set)
