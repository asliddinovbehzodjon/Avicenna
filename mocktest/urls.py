from rest_framework.routers import DefaultRouter
from .views import BotUsersViewset
from teacher.views import FanTestView,BlokTestlarView,CheckIt,CheckBlok
from django.urls import path,include
from resultimage.views import home
router = DefaultRouter()
router.register('newuser',BotUsersViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('fantest/<str:test_kodi>/<str:tel>/',FanTestView.as_view()),
    path('bloktest/<str:test_kodi>/<str:tel>/', BlokTestlarView.as_view()),
    path('checkfantest/<str:test_kodi>/', CheckIt.as_view()),
    path('checkbloktest/<str:test_kodi>/', CheckBlok.as_view()),
    path('getresult/',home)
]
