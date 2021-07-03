'''
Created Date: Friday July 2nd 2021 12:39:26 am
Author: Andrés X. Vargas
-----
Last Modified: Friday July 2nd 2021 12:51:07 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from django.urls import path
from.views import *

urlpatterns = [
    path('analyzer/', analyzer, name='analyzer'),
]
