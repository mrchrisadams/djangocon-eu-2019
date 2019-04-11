from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cool_chart/',
        views.my_cool_chart_view,
        name='my-cool-chart'
    ),
]
