from django.contrib import admin
from django.urls import include, path

import django_sql_dashboard

urlpatterns = [
    path("dashboard/", include(django_sql_dashboard.urls)),
    path("admin/", admin.site.urls),
]
