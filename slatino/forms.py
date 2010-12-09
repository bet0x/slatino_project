#from django.contrib.auth.models import User
#from django import forms
from django.utils.translation import ugettext_lazy as _
from supercaptcha import CaptchaField
from registration.forms import RegistrationFormUniqueEmail


class CustomRegistration(RegistrationFormUniqueEmail):

    captcha = CaptchaField(label=_(u'No robots here'))