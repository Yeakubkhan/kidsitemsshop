from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'city', 'district', 'color', 'quantity', 'total_price']

        total_price = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': True}))


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '  Your Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your City'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your District'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preferred Color'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Price'}),
        }
