"""FamilyNewsFeed URL Configuration

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
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter

"""
Import FamilyNewsFeed Views here with the syntax
from endpoints.<endpoint> import views as <endpoint>Views
"""

from endpoints.api.views import GuardianViewSet, PatientViewSet, ApprovedGuardianEventViewSet, \
    ApprovedPatientEventViewSet, GuardianPatientPairViewSet, GuardianNotificationInstanceViewSet, UserViewSet


router = DefaultRouter()
router.register(r'guardians', GuardianViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'approved-guardian-events', ApprovedGuardianEventViewSet)
router.register(r'approved-patient-events', ApprovedPatientEventViewSet)
router.register(r'guardian-patient-pairs', GuardianPatientPairViewSet)
router.register(r'guardian-notification-instances', GuardianNotificationInstanceViewSet)
router.register(r'users', UserViewSet)

"""
Import FamilyNewsFeed Views here with the syntax:

import endpoints.<endpoint>.views as <endpoint>Views
"""
import endpoints.welcome.views as welcomeViews
import endpoints.fhir_auth.views as fhirAuthViews
from endpoints.sms import sms

urlpatterns = [
    # django paths
    path('admin/', admin.site.urls),

    # FamilyNewsFeed Views
    path(r'welcome/', welcomeViews.welcome),
    path(r'teapot/', welcomeViews.teapot),
    re_path(r'^api/', include(router.urls)),
    path(r'send-update/', sms.receive_and_send_update),
    path('api-auth/', include('rest_framework.urls')),
    path('launch/', fhirAuthViews.oauth_handshake),
    # path('/', fhirAuthViews.oauth_handshake),
    path('redirect/', fhirAuthViews.redirect_callback),
]
