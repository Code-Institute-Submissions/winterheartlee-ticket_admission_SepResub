from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.ChoiceField(choices=[("buyer", "Buy Tickets"), ("creator", "Sell Tickets")])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user