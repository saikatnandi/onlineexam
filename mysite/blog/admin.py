from django.contrib import admin

# Register your models here.

from .models import *
from django.utils import timezone



class Tag_Admin(admin.ModelAdmin):
    exclude = ('pub_date', 'edit_date')


class Post_Admin(admin.ModelAdmin):
    exclude = ('pub_date', 'edit_date')
    search_fields = ('title_text', )
    list_display = ('title_text', 'user', 'pub_date', 'edit_date')
    filter_horizontal = ('tag',)
    list_filter = ( 'pub_date', 'edit_date'
                   )

    def save_model(self, request, obj, form, change):
        # print ("\n\n printing about obj " + str(obj))
        obj.update_date()
        obj.save()

class Comment_Admin(admin.ModelAdmin):
    exclude = ('pub_date', 'edit_date')

    def save_model(self, request, obj, form, change):
        # print ("\n\n printing about obj " + str(obj))
        obj.update_date()
        obj.save()






admin.site.register(Tag, Tag_Admin)
admin.site.register(Post, Post_Admin)
admin.site.register(Comment, Comment_Admin)