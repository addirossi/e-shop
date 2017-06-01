from django.conf import settings
from django.shortcuts import redirect


def is_anonymous(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated():
            return redirect(settings.REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper