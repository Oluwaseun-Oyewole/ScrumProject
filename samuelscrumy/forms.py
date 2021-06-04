from django import forms
from django import forms
from .models import ScrumyGoals
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']

        
class SelectGroupForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = Group
        fields = ['group' ]
    
    def __init__(self, *args, **kwargs):
        super(SelectGroupForm, self).__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Please select a group'


class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']


class UpdateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_status']