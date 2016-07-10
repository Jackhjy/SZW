from django.conf.urls import *
from IoT.views import  *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'userlogin/$', UserLoginV),
    url(r'userlogout/$', UserLogoutV),
    url(r'accounts/$', UserHomeV),
    url(r'home/$', UserHomeV),
    url(r'userprofile/$',login_required(UserProfileListV.as_view(),
    	login_url='/IoT/userlogin/'),name='userprofilelist'),
    url(r'userprofile/(?P<pk>\d+)/$',login_required(UserProfileDetailV.as_view(),
    	login_url='/IoT/userlogin/'),name='userprofiledetail'),
    url(r'userprofile/create/$',login_required(UserProfileCreateV.as_view(),
    	login_url='/IoT/userlogin/'),name='userprofilecreate'),
    url(r'userprofile/update/(?P<pk>\d+)/$',login_required(UserProfileUpdateV.as_view(),
    	login_url='/IoT/userlogin/'),name='userprofileupdate'),
    url(r'userprofile/delete/(?P<pk>\d+)/$',login_required(UserProfileDeleteV.as_view(),
    	login_url='/IoT/userlogin/'),name='userprofiledelete'),
    url(r'useraccess/$',login_required(UserAccessListV.as_view(),
    	login_url='/IoT/userlogin/'),name='useraccesslist'),
    url(r'region/$',login_required(RegionListV.as_view(),
    	login_url='/IoT/userlogin/'),name='regionlist'),
    url(r'region/(?P<region_pk>\d+)/$',login_required(RegionDetailV.as_view(),
    	login_url='/IoT/userlogin/'),name='regiondetail'),
    url(r'dev/$',login_required(DevListV.as_view(),
    	login_url='/IoT/userlogin/'),name='devlist'),
    url(r'dev/(?P<dev_pk>\d+)/$',login_required(DevDetailV.as_view(),
    	login_url='/IoT/userlogin/'),name='devdetail'),
    url(r'sensor/$',login_required(SensorListV.as_view(),
    	login_url='/IoT/userlogin/'),name='sensorlist'),
     url(r'sensor/(?P<sensor_pk>\d+)/$',login_required(SensorDetailV.as_view(),
    	login_url='/IoT/userlogin/'),name='sensordetail'),
     url(r'sensorthreshold/$',login_required(SensorThresholdListV.as_view(),
    	login_url='/IoT/userlogin/'),name='sensorthresholdlist'),
     url(r'sensorthreshold/create/(?P<sensor_id>\d+)/$',login_required(SensorThresholdCreateV.as_view(),
    	login_url='/IoT/userlogin/'),name='sensorthresholdcreate'),
     url(r'sensorthreshold/update/(?P<pk>\d+)/$',login_required(SensorThresholdUpdateV.as_view(),
            login_url='/IoT/userlogin/'),name='sensorthresholdupdate'),
     url(r'sensorthreshold/delete/(?P<pk>\d+)/$',login_required(SensorThresholdDeleteV.as_view(),
            login_url='/IoT/userlogin/'),name='sensorthresholddelete'),


     url(r'search/$',SearchV,name='sensorsearch'),
)
