from django import forms

class CreacionLibroFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    publicacion = forms.IntegerField()
    editorial = forms.CharField(max_length=30)

class BuscarLibro(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)