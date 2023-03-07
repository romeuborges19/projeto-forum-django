from django.contrib import admin
from .models import Category, Question

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    ...

admin.site.register(Question, QuestionAdmin)
