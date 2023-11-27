from django import forms
from .models import bookMark, catego

class bookMarkForm(forms.ModelForm):
    class Meta:
        model = bookMark
        fields = ['title','link','cate','rate']


class categoForm(forms.ModelForm):
    class Meta:
        model = catego
        fields = ['title']


