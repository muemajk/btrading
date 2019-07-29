from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Biotech.models import Product
from django_countries.fields import CountryField




class ProductForm(forms.Form):
	Item_Name = forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_prodname',
				 'placeholder':'Product name'
				 }
				 )
			)
	Brand_Name = forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_brandname',
				 'placeholder':'Brand name'
				 }
				 )
			)
	Units_in_Kg_litres_or_grams = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_Unit',
			 'placeholder':'Product Unit'
			 }
			 )
		)
	Unit_per_pack = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_pack',
			'placeholder':'Units in one package'
		 	}
			)
		)

	Price_In_USD = forms.IntegerField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_price',
			 'placeholder':'Your price for the product considering location cost'
			 }
			 )
		)

	Stock = forms.IntegerField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_stock',
			 'placeholder':'Your stock amount'
			 }
			 )
		)

	Description = forms.CharField(
		widget=forms.Textarea(
			attrs={'class' : 'form-control',
			'id': 'form_description',
			 'placeholder':'Give us a brief product description'
				}
			 )
		)
	city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'form_place','placeholder':'What city or town is the product from'}))

	Country_of_origin = CountryField(blank_label='(select country)').formfield()



	Attach_picture = forms.FileField()










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



class searchForm(forms.Form):
	search= forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_search',
				 'placeholder':'Search product'
				 }
				 )
			)
	def clean(self):
		data = self.cleaned_data
		ser = self.cleaned_data.get("search")

		return data
