from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path("login/", views.login_request, name='login'),
    path("logout/", views.logout_request, name='logout'),
    #path("profile/", views.view_profile, name='profile'),
    path("register/", views.register_st , name='reg-st'),

    path("ques/", views.doubt_form , name='ask-doubt'),
    path("ques/view", views.my_doubts , name='my-doubt'),
    #path("ques/solve", views.doubt_form , name='answer-doubt'),

    #path("del/<int:pk>", views.delete_student , name='delete-st'),
    #path("delt/<int:pk>", views.delete_teacher , name='delete-tech'),
]

