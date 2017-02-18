from django.shortcuts import render, redirect
from .forms import MessageForm

def index(request):
    message_form = MessageForm()
    return render(request,
                  'contactform/index.html',
                  {'message_form': message_form})

def create(request):
    message = MessageForm(request.POST)

    if message.is_valid():
        message.save()
        return redirect('/?message=success')
    else:
        return render(request,
                      'contactform/index.html',
                      {'message_form': message})
