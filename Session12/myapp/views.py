from django.shortcuts import render
from django.http import HttpResponse

# def set_session(request):
#     request.session['username'] = 'Dev'
#     request.session['course'] = 'Django'
#     return HttpResponse(f'session set successfully!!!')

# def get_session(request):
#     # uname = request.session.get('username','Guest')
#     # course = request.session.get('course','Not Enrolled')
#     if 'username' in request.session:
#         uname = request.session.get('username')
#         course = request.session.get('course')
#         print(uname,course )
#         return HttpResponse(f'Hey {uname},This is your {course}')
#     else:
#         return HttpResponse('No Session found')

# def delete_session(request):
#     # try:
#     #     del request.session['username']
#     #     del request.session['course']
#     # except:
#     #     pass
#     request.session.flush()
#     return HttpResponse(f'Session Deleted successfully!!!')


def setCookies(request):
    response = HttpResponse(f'Cookie Set successfully!!!')
    response.set_cookie('username','Dev',max_age=60*60*24)   # valid for 1 day
    response.set_cookie('course','Django',max_age=60*60*24)  # valid for 1 day
    return response

def getCookies(request):
    if 'username' in request.COOKIES:
        uname = request.COOKIES.get('username')
        course = request.COOKIES.get('course')
        print(uname)
        return HttpResponse(f'Hey {uname},This is your {course}')
    else:
        return HttpResponse(f'No Cookie Found')

def deleteCookies(request):
    response = HttpResponse(f'Cookie Deleted successfully!!!')
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response