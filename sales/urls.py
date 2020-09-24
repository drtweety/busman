from django.urls import path
from . import views

urlpatterns=[
    path('', views.invoicelist, name='sales-list'),
    path('create/', views.InvoiceCreateView.as_view(), name='sales-create'),
    path('<int:pk>/edit/', views.InvoiceUpdateView.as_view(), name='sales-edit'),
    path('<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='sales-delete'),
    path('<int:pk>/view/', views.InvoiceDetailView.as_view(), name='sales-view'),
    path('<int:pk>/invoice/add/',
         views.EntryCreateView.as_view(), name='sales-entry-add'),
]