from django.shortcuts import redirect

def auth_middleware(get_respond):
    def middleware(request):
        if not request.session.get('customer'):
           return redirect('login')
        respond = get_respond(request)

        return respond
    return middleware
