from django.contrib import admin
from .models import Question
from .models import Choice
from .models import Program

admin.site.register(Program)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class Prog