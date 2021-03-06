from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import os
import datetime
from django.core.urlresolvers import reverse
from .models import Message
from .forms import AddMessageForm
from .tasks import *

def index(request):
    response = {}
    error = False

    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            date = datetime.datetime.now()
            message = Message.objects.create(name=name, content=content, date=date)   
            check_bad_words_async.delay(message.pk,message.content)
            return HttpResponseRedirect(reverse(index))
        else:
            error = True
    else:
        form = AddMessageForm()

    response['error'] = error 
    response['form'] = form

    response['all_messages'] = Message.objects.all().order_by("-date")
    return render(request, 'index.html', response)
