from django.db import models
from django.forms import ModelForm, TextInput

class WifiGuest(models.Model):
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	email = models.CharField(max_length=300)
	def __str__(self):
		return self.email

class StoreInfo(models.Model):
	spu = models.CharField(max_length=200, blank=True)
	loyaltyurl = models.CharField(max_length=200, blank=True)
	store_name = models.CharField(max_length=200)
	def __str__(self):
		return self.store_name

class WifiGuestForm(ModelForm):
	store = models.ForeignKey(StoreInfo, on_delete=models.CASCADE)
	class Meta:
		model = WifiGuest
		fields = ['email']
		widgets = {
			'email' : TextInput(attrs={'placeholder': "Enter your email"})
		}
