from django.shortcuts import render
from django.http import HttpResponse 
from .models import *


def index(request): 
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal) 

def move_goal(request, goal_id):
  item = ScrumyGoals.objects.get(goal_id=goal_id)
  print(item)
  return HttpResponse(item.goal_name) 