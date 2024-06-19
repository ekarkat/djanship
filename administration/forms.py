from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, State, City


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
    state = forms.ModelChoiceField(
        queryset=State.objects.all().exclude(id=1),
        required=True,
        label='State',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'state-select'})
    )
    city = forms.CharField(
        max_length=50,
        required=True,
        label='City',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'city-select'})
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'phone']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Phone',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
    field_order = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'phone', 'state']


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
        state_name = self.cleaned_data.get('state')
        city_id = self.cleaned_data.get('city')

        state = State.objects.get(name=state_name)
        city = City.objects.get(id=city_id)

        userprofile = UserProfile.objects.create(
            user=user,
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone'),
            state=state,
            city=city
        )
        return userprofile


# Login Form
class LoginForm(forms.Form):
    # login form
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            print('This username is not registered')
            raise forms.ValidationError('This username is not registered')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                print('Invalid password')
                raise forms.ValidationError('Invalid password')
        return password
