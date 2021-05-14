from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

def thankyou(request):
    return render(request,'form/success.html')

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # check correct data
        if fm.is_valid():
            print('form validation')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password =fm.cleaned_data['password']

            # for showing data in terminal
            print(name)
            print(email)
            print(password)

            return HttpResponseRedirect('/makeform/success/')

    else:
        fm = StudentRegistration()
        # print("ye get request se aya hai")

    return render(request, "form/makeform.html", {'form': fm})
