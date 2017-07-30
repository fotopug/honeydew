from django.shortcuts import render, get_object_or_404
from .models import StoreInfo, WifiGuestForm

def index(request):
	stores_with_wifi = StoreInfo.objects.all()
	context = {
		'stores_with_wifi': stores_with_wifi,
		}
	return render(request,'honeypot/index.html',context)

def welcome(request, store_id):
	storeWelcome = get_object_or_404(StoreInfo, pk=store_id)
	form = WifiGuestForm()
	context = {
			'store': storeWelcome,
			'form':form
		}
	return render(request, 'honeypot/welcome.html', context)

def thanks(request, store_id):
	submit_email = get_object_or_404(StoreInfo, pk=store_id)
	context = {
		'store':submit_email
	}
	form = WifiGuestForm(request.POST)
	if form.is_valid():
		email_address = form.save(commit=False)
		email_address.post = submit_email
		email_address.save()
		return render(request, 'honeypot/thanks.html', context)
	else:
		return render(request, 'honeypot/thanks.html', context)

