from django import forms

from shop.accounts.models import MyUser


class SignIn(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': u'Enter your email'}),
            'password': forms.PasswordInput(attrs={'placeholder': u'Enter password'}),
        }


class SignUp(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': u'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': u'Фамилия'}),
            'email': forms.EmailInput(attrs={'placeholder': u'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': u'Пароль'})
        }

    def save(self):
        user = super(SignUp, self).save()
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user