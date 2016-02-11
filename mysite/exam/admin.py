from django.contrib import admin

from .models import Mcq_Question
from .models import Topic
from .models import Question_Set


admin.site.register(Mcq_Question)
admin.site.register(Topic)
admin.site.register(Question_Set)





