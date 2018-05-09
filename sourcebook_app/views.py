from django.shortcuts import render
from sourcebook_app.forms import rsvpForm
from sourcebook_app.models import rsvp
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = rsvpForm(request.POST)
		if form.is_valid():
			name = request.POST.get('name', None)
			email = request.POST.get('email', None)
			note = request.POST.get('note', None)
			rsvp1 = rsvp.objects.update_or_create(
                            name = name,
                            email = email,
                            note = note,
                            )
			message = 'Thank you, see you in Boston'
			return render(request, 'index.html', { 'message':message })

	else:
		form = rsvpForm()
		return render(request, 'index.html', { 'form':form })

def wind(request):
    return render(request, 'wind.html')
