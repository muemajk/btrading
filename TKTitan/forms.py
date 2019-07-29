from django import forms


class Checkoutform(forms.Form):
	Voucher_code =  forms.CharField(
		widget=forms.TextInput(
			attrs={'class' : 'form-control',
			'id': 'form_voucode',
			 'placeholder':'Your voucher code'
			 }
			 )
		)
	def clean(self):
		data = self.cleaned_data
		vcode = self.cleaned_data.get("Voucher_code")
		

		if vcode != "":
			raise forms.ValidationError("There are no Voucher at this moment!")
			print(password)
			print(conpass)
		return data		

class Productnumber(forms.Form):
	size =  forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'class' : 'form-control',
			'id': 'form_prodsize',
			 
			 }
			 )
		)
