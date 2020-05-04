from django import forms
from .models import Abonent

class StartForm(forms.Form):
    contract = forms.CharField(max_length=10)

    def work(self):
        abon = Abonent.get(contract=self.contract)
        print(abon)


