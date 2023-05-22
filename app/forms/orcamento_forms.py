from django import forms

from ..models import Orcamento


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'
        exclude = ['pac','data']