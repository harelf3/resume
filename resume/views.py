
from django.shortcuts import render
from django import forms
from .models import Customer


class EmailForm(forms.Form):
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form1','placeholder':'your email'}))
# Create your views here.

def index(request):
    if request.method =="POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            Email = form.cleaned_data['Email']
            Customer.objects.create(Email=Email)
            
            template = 'resume/index.html'
            context = {
                #<br><p>check out our social medias</p> put inside after social medias working 
                "messege":"Well Contact You Soon",
                "medias":1,
                "hidden":1
                }
            return render(request, template, context)
        else:
            form = EmailForm()
            context = {
            "messege":"We Think Your Email Is Invalid Want To Try Again?",
            "form" :form,
            }
            template = 'resume/index.html'
            return render(request, template, context)

    else:
        form = EmailForm()
        context = {
        "messege":"Want TO Be Different?",
        "form" :form,
        }
        template = 'resume/index.html'
        return render(request, template, context)
def scroll(request):
    template = 'resume/scroll.html'
    return render(request, template)

def ecommerce(request):
    template = 'resume/ecommerce.html'
    return render(request, template)

