from django.contrib import admin
from .models import Question,Answer,Like
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user','text','created_at']

class AnserAdmin(admin.ModelAdmin):
    list_display = ['user','question','text','created_at']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['user','answer']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnserAdmin)
admin.site.register(Like,LikeAdmin)
