from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
import random
from django.contrib.auth.models  import User

    
def index(request): 
  goal_name = ScrumyGoals.objects.filter(goal_name="Learn Django")
  return HttpResponse(goal_name) 

# def move_goal(request, goal_id):
#   goal_item = ScrumyGoals.objects.get(goal_id=goal_id)
#   return HttpResponse(goal_item.goal_name) 

def move_goal(request, goal_id):
    try:
      obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
      return render(request, 'samuelscrumy/exception.html', {'error': 'A record with that goal id does not exist'})
    else: return HttpResponse(obj.goal_name)
    
    
def add_goal(request):
  goals = ScrumyGoals.objects.create(
    goal_name = 'Keep Learning Django',
    goal_id = random.randint(1000, 9999),
    created_by = 'Louis',
    moved_by = 'Louis',
    owner = 'Louis',
    goal_status = GoalStatus.objects.get(status_name= "Weekly Goal"),
    user = User.objects.get(username='LouisOma')
  )
  return HttpResponse(goals)

# def home(request):
#       items = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")
#       output = ' '.join([eachgoal.goal_name for eachgoal in items])
#       return HttpResponse(output)

# def home(request):
#       return render(request, 'samuelscrumy/home.html', {"goal_name":'Learn Django',"goal_id":2,"user":User.objects.get(username='LouisOma')
#       })

def home(request):
  context = {'users':User.objects.all(),'WeeklyGoal':GoalStatus.objects.get(id=1).scrumygoals_set.all(),'DailyGoal':GoalStatus.objects.get(id=2).scrumygoals_set.all(), 
              'DoneGoal':GoalStatus.objects.get(id=4).scrumygoals_set.all()}
  return render(request, 'samuelscrumy/home.html', context)

