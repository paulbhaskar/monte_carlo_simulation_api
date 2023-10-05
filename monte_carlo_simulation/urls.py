from django.urls import re_path

from monte_carlo_simulation import views

urlpatterns = [
    re_path(r'^api/trials$', views.trial_list),
    re_path(r'^api/trials/(?P<pk>[A-Za-z0-9_-]+)$', views.trial_detail)
]
