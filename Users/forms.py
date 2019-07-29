from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Client
from django_countries.fields import CountryField



class LoginForm(forms.Form):
	username= forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_username',
				'placeholder':'Your username'
			 }
		 )		
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_password',
				 'placeholder':'Your password'
				 }
			 )
		)



class RegisterForm(forms.ModelForm):


	firstname = forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_firstname',
				 'placeholder':'Your firstname'
				 
				 }
				 )
			)
	lastname = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_lastname',
			 'placeholder':'Your lastname'
			 }
			 )
		)
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_username',
			 'placeholder':'Your username'
			 }
			 )
		)

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={'class' : 'form-control',
			'id': 'form_email',
			 'placeholder':'Your email address'
			 }
			 )
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_password',
				 'placeholder':'Your password'
				 }
			 )
		)
	confirm_password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_conpass',
				 'placeholder':'Confirm your password'
				 }
			 )
		)
	phone = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_phone_num',
			 'placeholder':'Your phone number'
			 }
			 )
		)
	Whatsapp_phone_number = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_alternate_phone',
			 'placeholder':'Your Whatsapp phone number'
			 }
			 )
		)
	We_Chat = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_alternate_phone',
			 'placeholder':'Your Wechat account(Optional*)'
			 }
			 )
		)	

	Skype = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_alternate_phone',
			 'placeholder':'Your Skype account(Optional*)'
			 }
			 )
		)		
	physical_address = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_physical_address',
			 'placeholder':'Your physical address'
			 }
			 )
		)

	country =  CountryField(blank_label='(select country)').formfield()




	class Meta:
		model = Client
		fields = ['privilege','role']

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		conpass = self.cleaned_data.get("confirm_password")

		if conpass != password:
			raise forms.ValidationError("The passwords must match!")
			print(password)
			print(conpass)
		return data


	def clean_username(self):
		username = self.cleaned_data.get('username')
		ps = User.objects.filter(username=username)
		if ps.exists():
			raise forms.ValidationError("An account with this username exists")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		pe = User.objects.filter(email = email)
		if pe.exists():
			raise forms.ValidationError("An account with this Email Address exists")
		return email








		

class emailform(forms.Form):
	"""docstring for emailform"""
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={'class' : 'form-control',
			'id': 'form_email',
			 'placeholder':'Your email address'
			 }
			 )
		)




class passwordupdateform(forms.Form):
	Current_password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_password',
				 'placeholder':'Your password'
				 }
			 )
		)

	New_password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_password',
				 'placeholder':'Your password'
				 }
			 )
		)
	confirm_password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={'class' : 'form-control',
				'id': 'form_conpass',
				 'placeholder':'Confirm your password'
				 }
			 )
		)
	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		conpass = self.cleaned_data.get("confirm_password")

		if conpass != password:
			raise forms.ValidationError("The passwords must match!")
			print(password)
			print(conpass)
		return data


class Privilegeform(forms.ModelForm):

	class Meta:
		model = Client
		fields = ['privilege']	


class roleform(forms.ModelForm):

	class Meta:
		model = Client
		fields = ['role']

class phoneUpdateform(forms.Form):
	phone = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_phone_num',
			 'placeholder':'Your phone number'
			 }
			 )
		)

class AltphoneUpdateform(forms.Form):
	phone = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_phone_num',
			 'placeholder':'Your phone number'
			 }
			 )
		)



class addressUpdateform(forms.Form):
	physical_address = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_address_to_change',
			 'placeholder':'Your physical address'
			 }
			 )
		)
