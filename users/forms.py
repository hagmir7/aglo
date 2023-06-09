from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
    def clean_username(self):
        cd = self.cleaned_data
        if not User.objects.filter(username=cd['username']).exists():
            raise ValidationError(_("Il n'y a pas d'utilisateur enregistré avec ce nom !"))
        return cd['username']




class SignUpForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')



class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label=_("Nom d'utilisateur"), max_length=30,help_text=_("Le nom d'utilisateur ne doit pas contenir d'espaces"),
         widget=forms.TextInput(attrs={'class': 'form-control input-size bg-secondary', 'placeholder': _("Nom d'utilisateur")}))
    username = forms.CharField(label=_("Nom d'utilisateur"), max_length=30,help_text=_("Le nom d'utilisateur ne doit pas contenir d'espaces"), widget=forms.TextInput(
        attrs={'class': 'form-control input-size', 'placeholder': _("Nom d'utilisateur")}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': _('Email')}))
    first_name = forms.CharField(label=_('Prénom'), widget=forms.TextInput(
        attrs={'class': 'form-control input-size', 'placeholder': _('Prénom')}))
    last_name = forms.CharField(label=_('Nome'),widget=forms.TextInput(
        attrs={'class': 'form-control input-size ', 'placeholder': _('Nome')}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control input-size', 'placeholder': _('Password')}), min_length=8)
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control input-size', 'placeholder': _('Confirm Password')}), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError(_('Le mot de passe ne correspond pas.'))
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise ValidationError(_('Il y a un utilisateur enregistré avec ce nom !'))
        return cd['username']



    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError(_("Il y a un utilisateur enregistré avec cet e-mail !"))
        return cd['email']    




class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'phone', 'country' )


class UserUpdateInfo(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def clean(self):
        cleaned_data = super(PasswordChange, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two passwords did not match'))
        return cleaned_data




