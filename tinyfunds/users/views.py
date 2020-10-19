from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render

from .models import User

class AccountView(generic.DetailView):
    template_name = 'account/account.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return User.objects

def user(request, pk):
    user = get_object_or_404(User, id=pk)
    if (request.method == "POST"):
        new_name = request.POST['name']
        new_bio = request.POST['bio']
        if new_name != "":
            user.name = new_name
        if new_bio != "":
            user.bio = new_bio
        user.save()
    return render(request, 'account/account.html', {
        'user': user,
    })
