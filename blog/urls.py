"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

'''
一直出现这个错误，然后 可能是 include 路径出错
django.core.exceptions.ImproperlyConfigured: 
The included URLconf 'blog.urls' does not appear to have any patterns in it.
 If you see valid patterns in the file then the issue is probably caused by a circular import.
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myblog/', include('myblog.urls')),

]

