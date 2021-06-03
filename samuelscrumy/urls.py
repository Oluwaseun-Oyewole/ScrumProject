from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'samuelscrumy'

urlpatterns = [
    path('', views.index, name="about",),
    path('movegoal/<int:goal_id>/', views.move_goal, name="movegoal"),
    path('addgoal/', views.add_goal, name="addgoal"),
    path('home/', views.home, name="home"),
    path('creation/', views.creation, name="creation"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.test_group, name="test"),
        
    # extra
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    # path("group", views.SelectGroupView.as_view(), name="select"),
    path("addgroup/<int:id>/", views.add_group, name="select")

    
]