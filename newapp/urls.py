# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('order/', views.order_product, name='order_product'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.user_login, name='login'),
#     path('register/', views.register, name='register'),
#     path('vote/<int:item_id>/', views.vote, name='vote'),

#          path('vote_result/', views.vote_result, name='vote_result'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('vote/', views.index, name='index'),
]
