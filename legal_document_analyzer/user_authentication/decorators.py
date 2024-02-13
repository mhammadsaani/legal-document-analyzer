from django.http import HttpResponseRedirect

def is_authenticated(view_function):
    def check_if_authenticated(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/auth/unauthorized/')
        return view_function(request)
    return check_if_authenticated