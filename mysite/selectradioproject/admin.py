from django.contrib import admin
from .models import Question
from .models import Choice
from .models import Program

admin.site.register(Program)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class ProgramInline(admin.StackedInline):
    model = Program
    extra = 4
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    list_display = ['question_text','pub_date','was_published_recently']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
    
class ChioceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['choice_text']}),
        ('Votes',{'fields':['votes'],'classes':['collapse']}),
    ]
    search_fields = ['question_text']
    inlines = [ProgramInline]
admin.site.register(Choice,ChioceAdmin)