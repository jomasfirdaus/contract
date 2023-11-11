from django import forms
from rekrutamentu.models import UserApplication, UserAttachment
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from contract.models import *



class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'  # You can specify the fields you want to include if needed

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('contract_type', css_class='col-md-4'),
            ),

            Row(
                Column('grade', css_class='col-md-4'),
                Column('position', css_class='col-md-4'),
                Column('nivel', css_class='col-md-4'),
            ),

            Row(
                Column('division', css_class='col-md-4'),
                Column('department', css_class='col-md-4'),
            ),

            Row(
                Column('start_date', css_class='col-md-6'),
                Column('end_date', css_class='col-md-6'),
            ),
            
            Row(
                Column('file', css_class='col-md-6'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['contract_type'].widget.attrs['class'] = 'form-control'
        self.fields['grade'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['nivel'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'
        self.fields['file'].widget.attrs['class'] = 'form-control'
  