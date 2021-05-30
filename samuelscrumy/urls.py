from django.urls import path, include
from . import views

app_name = 'samuelscrumy'

urlpatterns = [
    path('', views.index, name="about",),
    path('movegoal/<int:goal_id>/', views.move_goal),
    path('addgoal/', views.add_goal, name="addgoal"),
    path('home/', views.home, name="account"),
    path('accounts/', include('django.contrib.auth.urls'),)
]