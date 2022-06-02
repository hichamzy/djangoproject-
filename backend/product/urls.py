from django.urls import path

from . import views


urlpatterns=[

   path('create/',views.product_create_view) , #create view
   path('<int:pk>/',views.product_detail_view) , #pk id of product api/product/3 for exemple
   path('list_create/',views.product_list_create_view),
   path('<int:pk>/update',views.product_update_view),
   path('<int:pk>/delete',views.product_delete_view),
   path('products/',views.product_list_view),
   path('search/',views.product_search)
]