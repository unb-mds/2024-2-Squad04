from django.contrib.auth.views import LoginView

class login_view(LoginView):
    template_name = 'login/login.html'
