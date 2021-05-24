from django.contrib import admin
from samuelscrumy.models import ScrumyGoals, ScrumyHistory, GoalStatus

# Register your models here.

admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)
