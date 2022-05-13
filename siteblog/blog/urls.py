import debug_toolbar
from django.urls import path, include


from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
]