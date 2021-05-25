from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
import random
from django.contrib.auth.models  import User

    
# def index(request): 
#   goal_name = ScrumyGoals.objects.filter(goal_name="Learn Django")
#   return HttpResponse(goal_name) 

def move_goal(request, goal_id):
  goal_item = ScrumyGoals.objects.get(goal_id=goal_id)
  return HttpResponse(goal_item.goal_name) 

def add_goal(request):
  ScrumyGoals.objects.create(
    goal_name = 'Keep Learning Django',
    goal_id = random.randint(1000, 9999),
    created_by = 'Louis',
    moved_by = 'Louis',
    owner = 'Louis',
    goal_status = GoalStatus.objects.get(id=1),
    user = User.objects.get(username='louis') 
  )
  return HttpResponse('new item created')

def home(request):  
  items = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")
  output = ' '.join([eachgoal.goal_name for eachgoal in items])
  return HttpResponse("The goal name " + output + " should be displayed on the webpage")


    
def index(request):
  goal_items = {
    "goal_name":"Learn Django",
    "goal_id": 2,
    "user":User.objects.get(username='louis')
  }
  return render(request, 'samuelscrumy/home.html', context={"goal_items":goal_items})
