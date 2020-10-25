from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash, name='org-dash'),
    path('none/', views.noOrgView, name='org-none'),
    path('create/', views.OrganizationCreateView.as_view(), name='org-create'),
    # path('join/', views.join_organization, name='org-join'),
    path('join/', views.OrganizationRequestFormView.as_view(), name='org-join'),


]
