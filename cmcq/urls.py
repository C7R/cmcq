"""cmcq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from filter import views
urlpatterns = [
     path('admin/', admin.site.urls),
    # path('', views.signup),
    # path('signup', views.signup),
    # path('login_func', views.login_func),
    # path('question/', views.question),
    # path('filter/',views.filter),
    # path('logout/', views.logoutfunc),
    # path('login/', views.login_page),

    url(r'^register$', views.signup_page),
    url(r'^$', views.login_page),
    url(r'^login_func$', views.login_func),
    url(r'^question$', views.question),
    url(r'^filter$', views.filter),
    url(r'^leaderboard$', views.lb),
    url(r'^logout$', views.logoutfunc),
    url(r'^signup', views.signup),
]
