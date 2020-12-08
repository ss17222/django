from django import forms
from mild.models import *

class SignUpForm(forms.ModelForm):
    class Meta:
        model =MyUser
        fields = ("__all__")

class EditForm(forms.ModelForm):
    class Meta:
        model =MyUser
        fields = ("email","fname","phone_number","lname","dob")
class ForgotForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields= ('email',)