from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'signup/',views.signup,name='signup'),
    url(r'login/',views.login,name='login'),
    url(r'home/',views.home,name='home'),
    url(r'employeepopup/',views.employeepopup,name='employeepopup'),
    url(r'merchantspopup/',views.merchantspopup,name='merchantspopup'),
    url(r'merchant1/',views.merchant1,name='merchant1'),
    url(r'merchant2/',views.merchant2,name='merchant2'),
    url(r'thanks_m1/',views.thanks_m1,name='thanks_m1'),
    url(r'thanks_m2/',views.thanks_m2,name='thanks_m2'),
    url(r'womenupload/',views.womenupload,name='womenupload'),
    url(r'women1/',views.women1,name='women1'),
    url(r'thanks_w1/',views.thanks_w1,name='thanks_w1'),
    url(r'job/',views.job,name='job'),
    url(r'apply/',views.apply,name='apply'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)