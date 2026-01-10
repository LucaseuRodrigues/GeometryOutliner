from django import forms


class CoordinatesModelForm(forms.Form):
    Edgesquantity = forms.IntegerField(min_value=3, max_value=10)
    Latvalue = forms.FloatField()
    Longvalue = forms.FloatField()
