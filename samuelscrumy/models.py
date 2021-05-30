from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT


# Create your models here.

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=30)
    moved_by = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    goal_status = models.ForeignKey('GoalStatus', on_delete=PROTECT)
    user = models.ForeignKey(User,  related_name='user', on_delete=models.CASCADE)
    
    # class Meta:
    #     verbose_name_plural = 'ScrumyGoals'
     
    def __str__(self):
        return self.goal_name
    
class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    moved_from = models.CharField(max_length=30)
    moved_to = models.CharField(max_length=30)
    time_of_action = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
     
    # class Meta:
    #     verbose_name_plural = 'ScrumyHistory'
        
    def __str__(self):
        return self.created_by

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)
     
    # class Meta:
    #     verbose_name_plural = 'GoalStatuses'
        
    def __str__(self):
        return self.status_name
    
    