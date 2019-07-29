from django import forms
from django.contrib.auth.models import User
from ecommerce.models import  Product


class Contactform(forms.Form):
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
	phone = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_phone_num',
			 'placeholder':'Your phone number'
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

	#def clean_email(self):
		#email = self.cleaned_data.get("email")
		#if not re.match('[^@]+@[^@]+\.[^@]+',email):
		#raise forms.ValidationError()
			#return email



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



class RegisterForm(forms.Form):
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



class UserForm(forms.Form):
		phone = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_phone_num',
			 'placeholder':'Your phone number'
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


		country = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_country',
			 'placeholder':'Your country'
			 }
			 )
		)




class Checkoutform(forms.Form):
	Voucher_code =  forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_voucode',
			 'placeholder':'Your voucher code'
			 }
			 )
		)
		

class Productnumber(forms.Form):
	size =  forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'class' : 'form-control',
			'id': 'form_prodsize',
			 
			 }
			 )
		)
