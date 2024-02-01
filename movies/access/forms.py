from django.forms import ModelForm
from access.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']