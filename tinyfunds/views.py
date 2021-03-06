import random
from decimal import Decimal

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from .models import Event, Pledge
from .users.models import User
from .models import Event
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
from .forms import CreateEventForm
from paypal.standard.forms import PayPalPaymentsForm

class HomeView(generic.ListView):
    template_name = 'tinyfunds/index.html'

    def get_queryset(self):
        return User.objects.all().order_by("-date_joined")

class ExploreView(generic.ListView):
    template_name = 'tinyfunds/explore.html'
    content_object_name = 'event_list' 

    def get_queryset(self):
        return Event.objects.all().order_by("-pub_date")

class UserView(generic.ListView):
    template_name = 'tinyfunds/users.html'
    content_object_name = 'user_list' 

    def get_queryset(self):
        return User.objects.all().order_by("-date_joined")


class UserViewDonated(generic.ListView):
    template_name = 'tinyfunds/users.html'
    content_object_name = 'user_list' 

    def get_queryset(self):
        return User.objects.all().order_by("-total_donated")

class UserViewVol(generic.ListView):
    template_name = 'tinyfunds/users.html'
    content_object_name = 'user_list' 

    def get_queryset(self):
        return User.objects.all().order_by("-total_hours_pledged")



class EventView(generic.DetailView):
    template_name = 'tinyfunds/event.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Event.objects

class CreateEventView(CreateView):

    template_name = 'tinyfunds/create_event.html'
    form_class = CreateEventForm


    def get(self, request, *args, **kwargs):
        context = {'form': CreateEventForm()}
        return render(request, 'tinyfunds/create_event.html', context=context)
    

    def post(self, request, id=None, template_name='tinyfunds/create_event.html'):
        if id:
            event = get_object_or_404(Event, pk=id)
            if event.user != request.user:
                return HttpResponseForbidden()
        else:
            event = Event()

        form = CreateEventForm(request.POST or None, instance=event)
        if request.POST and form.is_valid():
            form.save()

            # Save was successful, so redirect to another page
            return HttpResponseRedirect(reverse('event', args=[event.id]))

        return render(request, 'tinyfunds/create_event.html', {
                'form':form,
                'invalid':True,
            })
    

def event(request, pk):
    event = get_object_or_404(Event, id=pk)

    if (request.method == "POST"):
        new_title = request.POST['title'].strip()
        new_org_name = request.POST['org_name'].strip()
        new_pic = request.POST['pic'].strip()
        new_description = request.POST['description'].strip()
        new_event_date = request.POST['event_date'].strip()
        new_address = request.POST['address'].strip()
        new_goal = request.POST['goal'].strip()
        if new_title != "":
            event.title = new_title
        if new_description != "":
            event.description = new_description
        if new_org_name != "":
            event.org_name = new_org_name
        if new_pic != "":
            event.pic = new_pic
        if new_goal != "":
            event.money_goal = Decimal(new_goal)
        event.save()
    return HttpResponseRedirect(reverse('event', args=[pk]))

def pledge(request, pk):
    event = get_object_or_404(Event, id=pk)
    if (request.method == "POST"):
        user_id = request.POST['user_id'].strip()
        payment_amount = Decimal(request.POST['amount'].strip())
        payment_text = request.POST['text'].strip()
        p = Pledge(event=event, payer_id=user_id, payment_text=payment_text, payment_amount=payment_amount)
        p.save()
        event.pledge_set.add(p)
        event.save()
    return HttpResponseRedirect(reverse('event', args=[pk]))

def pledge_hours(request, pk):
    event = get_object_or_404(Event, id=pk)
    if (request.method == "POST"):
        user_id = request.POST['user_id'].strip()
        hours_amount = Decimal(request.POST['amount'].strip())
        payment_text = request.POST['text'].strip()
        p = Pledge(event=event, payer_id=user_id, payment_text=payment_text, hours_amount=hours_amount)
        p.save()
        event.pledge_set.add(p)
        event.save()
    return HttpResponseRedirect(reverse('event', args=[pk]))

def checkout(request, pk):
    event = get_object_or_404(Event, id=pk)
    context = {'event': event}
    return render(request, 'tinyfunds/donate.html', context)

def confirm(request, pk):
    event = get_object_or_404(Event, id=pk)
    if (request.method == "POST"):
        p_id = Decimal(request.POST['p_id'].strip())
        p = get_object_or_404(Pledge, id=p_id)
        u_id = Decimal(request.POST['u_id'].strip())
        u = get_object_or_404(User, id=u_id)
        p.confirm()
        if (p.payment_amount != None):
            event.add_money(p.payment_amount)
            u.add_money(p.payment_amount)
        else:
            event.add_hours(p.hours_amount)
            u.add_hours(p.hours_amount)
        p.save()
        event.save()
        u.save()
    return HttpResponseRedirect(reverse('event', args=[pk]))

def confirm_paypal(request):
    if (request.method == "POST"):
        user_id = Decimal(request.POST['u_id'].strip())
        u = get_object_or_404(User, pk=user_id)
        event = get_object_or_404(Event, pk=request.POST['dono_id'].strip())
        payment_amount = Decimal(request.POST['dono_amount'])
        payment_text = "Paypal donation!"
        p = Pledge(event=event, payer_id=user_id, payment_text=payment_text, payment_amount=payment_amount)
        p.confirm()
        if (p.payment_amount != None):
            event.add_money(p.payment_amount)
            u.add_money(p.payment_amount)
        else:
            event.add_hours(p.hours_amount)
            u.add_hours(p.hours_amount)
        p.save()
        u.save()
        event.pledge_set.add(p)
        event.save()
    return HttpResponseRedirect(reverse('event', args=[request.POST['dono_id']]))

def donate(request, pk, user_id):
    event = get_object_or_404(Event, id=pk)
    user = get_object_or_404(User, id=user_id)
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "donation for {}".format(event.title),
        "invoice": "invoice{}".format(random.randint(10,99)),
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('event', args=[pk])),
        "cancel_return": request.build_absolute_uri(reverse('event', args=[pk])),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
                "form": form,
                "event": event,
                "paying_user": user,
            }
    return render(request, "tinyfunds/payment.html", context)
  
def update_view(request, pk): 
    obj = get_object_or_404(Event, id=pk)
    form = CreateEventForm(request.POST or None, instance = obj) 
    context = {
        "form": form,
        "event": obj,
    }
      
    if (request.method == "POST"):
        if form.is_valid(): 
            form.save() 
        return HttpResponseRedirect(reverse('event', args=[pk]))
    else:
        return render(request, "tinyfunds/update_event.html", context)

def delete(request, pk):
    obj = get_object_or_404(Event, id=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('explore'))

def categoryFilter(request):
    if request.method == 'POST':
        if(request.POST.get('state') == 'N/A' and request.POST.get('categories') == 'N/A'):
            filteredDonations = Event.objects.all()
        elif (request.POST.get('state') != 'N/A' and request.POST.get('categories') != 'N/A'):
            filteredDonations = Event.objects.filter(state = request.POST.get('state'), category = request.POST.get('categories'))
        elif (request.POST.get('state') == 'N/A' and request.POST.get('categories') != 'N/A'):
            filteredDonations = Event.objects.filter(category = request.POST.get('categories'))
        elif(request.POST.get('state') != 'N/A' and request.POST.get('categories') == 'N/A'):
            filteredDonations = Event.objects.filter(state = request.POST.get('state'))
        return render(request, 'donation/index.html', {'active_donation_list':filteredDonations})

