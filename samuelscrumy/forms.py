from django import forms
from django import forms
from .models import ScrumyGoals
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple


class SignupForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2', 'group' ]



# class SelectGroupForm(UserCreationForm):
#     group = forms.ModelChoiceField(queryset=Group.objects.all(),
#                                    required=True)
#     class Meta:
#         model = User
#         fields = ['group']
        
class SelectGroupForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = Group
        fields = ['group', 'permissions', ]
        # fields = '__all__'
        widgets = {
            'permissions': FilteredSelectMultiple("Permission", False, attrs={'rows':'2'}),
        }
        

class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner']


class UpdateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_status']