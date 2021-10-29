from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Meetup,Participant
from .forms import RegisterationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all() # static method of models.Model
    return render(request, 'meetups/index.html',{
        'meetups' : meetups
    })

def meetup_details(request, meetup_slug):
    try:
        selected = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            form = RegisterationForm()
            return render(request, 'meetups/meetup-details.html', {
                'found' : True,
                'meetup' : selected,
                'form' : form
        })
        else:
            form = RegisterationForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                participant,was_Created = Participant.objects.get_or_create(email=user_email)
                selected.participants.add(participant)
                print(selected)
                return redirect('confirmation', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
                'found' : True,
                'meetup' : selected,
                'form' : form
        })

    except:
       return render(request, 'meetups/meetup-details.html', {
            'found' : False
        }) 

def success(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/success.html',{
        'organizer_email' :  meetup.organizer_email
    })