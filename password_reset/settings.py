import importlib
from django.conf import settings

PASSWORD_RECOVERY_FORM = getattr(settings, 'PASSWORD_RECOVERY_FORM', 'password_reset.forms.PasswordRecoveryForm')
PASSWORD_RESET_FORM = getattr(settings, 'PASSWORD_RESET_FORM', 'password_reset.forms.PasswordResetForm')

