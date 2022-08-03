from django import forms
from .models import db


class Projectform(forms.ModelForm):

    class Meta:
        model = db
        fields = '__all__'
        labels = {
            'R_T':'R&T',
            'Smart_req':'SMART REQ'
        }

    def __init__(self, *args, **kwargs):
        super(Projectform,self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
        self.fields['smart'].required = False
        self.fields['Address'].required = False
        self.fields['Abbr_id'].required = False
        self.fields['Proc_id'].required = False
