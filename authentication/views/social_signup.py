from allauth.account.views import SignupView


class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "users/custom_signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...

def test():
    for i in range(0,100):
        print(i)