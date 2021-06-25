from django import forms

from .models import Cell

class CellForm(forms.ModelForm):

    class Meta:
        model = Cell
        fields = '__all__'

    def clean(self):

        # data from the form is fetched using super function
        super(CellForm, self).clean()

        # extract the username and text field from the data
        time = self.cleaned_data.get('time')

        # conditions to be met for the username length
        if len(time) < 3:
            self._errors['time'] = self.error_class([
                'Minimum 5 characters required'])

        # return any errors if found
        return self.cleaned_data
