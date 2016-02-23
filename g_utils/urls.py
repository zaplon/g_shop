from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'render-form/', render_form, name='render-form')
]