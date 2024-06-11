from django import forms

from .models import UserProfile
from django.contrib.auth.models import User



# Register From
class RegisterForm(forms.ModelForm):
    # register form
    username = forms.CharField(
        max_length=50,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        max_length=50,
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'image']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Phone',
            'address': 'Address',
            'image': 'Image'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Explicitly set the order of the fields
        self.order_fields(['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name', 'phone', 'address', 'image'])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('Password must be at least 6 characters long')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already registered')
        return username

    def save(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')
        user = User.objects.create_user(username=username, password=password)
        userprofile = UserProfile.objects.create(
            user=user,
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone'),
            address=self.cleaned_data.get('address'),
            image=self.cleaned_data.get('image')
        )
        return userprofile