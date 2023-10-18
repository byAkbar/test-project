from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Question)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_id', 'question_text', 'answer_text', 'created_date']
