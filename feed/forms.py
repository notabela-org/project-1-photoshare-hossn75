from django import forms
from users.models import Profile

class EditProfileForm(forms.ModelForm):
    
    username = forms.CharField(max_length=150,required=False)
    class Meta:
        model = Profile
        fields = ('bio','image')

        widget = {
            'bio': forms.TextInput(attrs={'placeholder':'Bio'}),
            'image': forms.FileInput()
        }