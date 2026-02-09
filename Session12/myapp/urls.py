from django.urls import path
from .views import *
urlpatterns = [
    # path('set_session/',set_session),
    # path('get_session/',get_session),
    # path('delete_session/',delete_session),

    path('set_cookie/',setCookies),
    path('get_cookie/',getCookies),
    path('delete_cookie/',deleteCookies),
]
