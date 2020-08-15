from django.utils.deprecation import MiddlewareMixin


class SessionKiller(MiddlewareMixin):
    def process_request(self, request):
        print('Session Killer' + '\n' + 40*'=')
        if request.session.get('remember_me', 'No') == 'No':
            request.session['remember_me'] = True