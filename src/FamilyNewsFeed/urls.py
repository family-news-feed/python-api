'''FamilyNewsFeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path

'''
Import FamilyNewsFeed Views here with the syntax:

import endpoints.<endpoint>.views as <endpoint>Views
'''
import endpoints.welcome.views as welcomeViews
import endpoints.fhir_auth.views as fhirAuthViews

urlpatterns = [
    # django paths
    path('admin/', admin.site.urls),

    # FamilyNewsFeed Views
    path('welcome/', welcomeViews.welcome),
    path('teapot/', welcomeViews.teapot),
    path('launch/', fhirAuthViews.oauth_handshake),
    # path('/', fhirAuthViews.oauth_handshake),
    path('redirect/', fhirAuthViews.redirect_callback),
]
