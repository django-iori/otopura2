from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupview),
    path('userinfo/', userinfoview),
    path('login/', loginview),
    path('mypageapi/', MyPageView.as_view()),
    #path('login/', LoginView.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),
    #path('csrf_cookie/', set_csrf_token),
    path('csrf_cookie/', CsrfView),
    path('logout/', LogoutView.as_view()),
    path('authenticated/', authview),
    path('auth/', CheckAuthenticatedView.as_view()),
    #path('authenticated/', ExampleView.as_view()),
    path('upload/', uploadview),
    path('good/', goodview),
    path('upload_list/', UploadListView.as_view()),
    path('good_list/', Good_ListView.as_view()),
    path('comment/', commentview),
    path('comment_list/', Comment_ListView.as_view()),
    path('account/', AccountView.as_view()),
    path('hello/', HelloWorld),
    path('edit/', edit_profile),
    path('band/', BandView.as_view()),
    path('signout/', signoutview),
    path('delete_upload/', delete_upload),
]