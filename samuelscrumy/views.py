from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
import random
from django.contrib.auth.models  import User
from .forms import SignupForm, CreateGoalForm
from django.contrib.auth.models import Group

    
# def index(request): 
#   goal_name = ScrumyGoals.objects.filter(goal_name="Learn Django")
#   return HttpResponse(goal_name) 

        # my_group = Group.objects.get(name="Developer")
        # my_group.user_set.add(form)
        
def index(request): 
  if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
              form.save()
              user = User.objects.filter().last()
              my_group = Group.objects.get(name="Developer")
              my_group.user_set.add(user)
              return redirect('/samuelscrumy')
  else:
    form = SignupForm()
  return render(request, 'samuelscrumy/index.html', {'form': form})
  

# def move_goal(request, goal_id):
#   goal_item = ScrumyGoals.objects.get(goal_id=goal_id)
#   return HttpResponse(goal_item.goal_name) 

def move_goal(request, goal_id):
    try:
      obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
      return render(request, 'samuelscrumy/exception.html', {'error': 'A record with that goal id does not exist'})
    else: return HttpResponse(obj.goal_name)
    
    
# def add_goal(request):
#   goals = ScrumyGoals.objects.create(
#     goal_name = 'Keep Learning Django',
#     goal_id = random.randint(1000, 9999),
#     created_by = 'Louis',
#     moved_by = 'Louis',
#     owner = 'Louis',
#     goal_status = GoalStatus.objects.get(status_name= "Weekly Goal"),
#     user = User.objects.get(username='LouisOma')
#   )
#   return HttpResponse(goals)

def add_goal(request):
    if request.method == 'POST':
          form = CreateGoalForm(request.POST)
          if form.is_valid():
                form.save(commit=False)
                form.goal_id = 3
                form.goal_status =GoalStatus.objects.filter().last()
                form.save()
                return redirect('/samuelscrumy/home')
    else:
          form = CreateGoalForm()
    return render(request, 'samuelscrumy/addgoal.html', {'form': form})
      
          

# def home(request):
#       items = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")
#       output = ' '.join([eachgoal.goal_name for eachgoal in items])
#       return HttpResponse(output)

# def home(request):
#       return render(request, 'samuelscrumy/home.html', {"goal_name":'Learn Django',"goal_id":2,"user":User.objects.get(username='LouisOma')
#       })

def home(request):
  users = User.objects.all()
  WeeklyGoal=GoalStatus.objects.get(id=1)
  DailyGoal=GoalStatus.objects.get(id=2)
  VerifyGoal=GoalStatus.objects.get(id=3)
  DoneGoal=GoalStatus.objects.get(id=4)
  context = {'users':users,'WeeklyGoal':WeeklyGoal, 'DailyGoal':DailyGoal, 
             'VerifyGoal':VerifyGoal,
             'DoneGoal':DoneGoal}        
  return render(request, 'samuelscrumy/home.html', context)

  