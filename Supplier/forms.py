from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




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
	Unit = forms.IntegerField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_Unit',
			 'placeholder':'Product Unit'
			 }
			 )
		)
	Packaging = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_brandname',
			'placeholder':'Brand name'
		 	}
			)
		)

	Price = forms.IntegerField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_price',
			 'placeholder':'Your price'
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


	Country_of_origin = forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_description',
			 'placeholder':'Where is the item from'
				}
			 )
		)


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