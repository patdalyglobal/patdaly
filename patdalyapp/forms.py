from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from .models import ContactMessage
from django import forms
from .models import Project, Contractor, Supervisor
from django_ratelimit.decorators import ratelimit



class ContactMessageForm(forms.ModelForm):
    # Add the reCAPTCHA field to your form
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message']




#-------------------------- For Plateau State Ministry of Budget and Planning-------------#
# forms.py
class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'address', 'phone_number', 'rc_number']


class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['name', 'department', 'id_number']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    #def __init__(self, *args, **kwargs):
        #super(ProjectForm, self).__init__(*args, **kwargs)
        #self.fields['name'].queryset = Contractor.objects.all()
        #self.fields['name'].queryset = Supervisor.objects.all()
