from django.core import validators
import django.forms

class StudentRegistration(django.forms.Form):
    name= django.forms.CharField(error_messages={'required' : "enter your name"})
    email= django.forms.EmailField(error_messages={'required':"enter your email"},min_length=5,max_length=50)
    password=django.forms.CharField(error_messages={'required':"enter your password"},min_length=5,max_length=50)







