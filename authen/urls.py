from django.urls import path
from .views import index,signup,login_view,logout_view
urlpatterns = [
    path('',index,name='index'),
    path('signup/', signup,name='signup'),
    path('login/', login_view,name='auth_login'),
    path('logout/',logout_view,name='auth_logout')
]
