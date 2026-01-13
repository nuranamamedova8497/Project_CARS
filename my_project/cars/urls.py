from django.urls import path
from cars.views import (cars_list, car_detail, car_create,
                        car_edit, car_delete, send_deal_request,
                        owner_deal_requests_list, approve_deal_request, reject_deal_request,
                        owner_deal_requests_approved_list, owner_deal_requests_rejected_list)


app_name = 'cars'


urlpatterns=[
    path('', cars_list, name='cars_list'),
    path('<int:car_id>/', car_detail, name='car_detail'),
    path('add/', car_create, name="car_create"),
    path('<int:car_id>/edit/', car_edit, name='car_edit'),
    path('<int:car_id>/delete/', car_delete, name='car_delete'),
    path('<int:car_id>/deal-request/', send_deal_request, name='send_deal_request'),
    path('my-deal-requests/', owner_deal_requests_list, name='owner_deal_requests_list'),
    path('request/<int:deal_request_id>/approve/', approve_deal_request, name='approve_deal_request'),
    path('request/<int:deal_request_id>/reject/', reject_deal_request, name='reject_deal_request'),
    path('my_approved-deal-requests/', owner_deal_requests_approved_list, name='owner_deal_requests_approved_list'),
    path('my_rejected-deal-requests/', owner_deal_requests_rejected_list, name='owner_deal_requests_rejected_list')
]

