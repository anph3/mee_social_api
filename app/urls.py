from django.urls import path
from configs.variable_system import FILES
from .views.auth_view import *
from .views.fail_request import custom404

all_url = {
    'url_auth':[
        path('login', AuthView.as_view({'post':'login'}), name='login'),
        path('refresh-token', AuthView.as_view({'post':'refresh_token'}), name='refresh_token'),
        path('register', AuthView.as_view({'post':'register'}), name='register'),
    ]
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]

handler404 = custom404