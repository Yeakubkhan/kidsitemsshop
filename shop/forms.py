from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'city', 'district', 'color', 'quantity', 'total_price']

        total_price = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': True}))


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'নাম লিখুন'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '  আপনার সচল মোবাইল নাম্বার'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '  গ্রাম/ঠিকানা', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'আপনার থানা'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'আপনার জেলা'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'পছন্দের কালার টি/কালার গুলো লিখুন'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', }),
        }
