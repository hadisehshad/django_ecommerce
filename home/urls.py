from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    # for retrieving the list of testimonials and creating a new one
    path('api/v2/testimonials', TestimonialListCreateView.as_view(), name='testimonial-list-create'),

    # for retrieving or updating a specific testimonial
    path('api/v2/testimonials/<int:pk>', TestimonialDetailView.as_view(), name='testimonial-detail'),

    #  for deleting a specific testimonial (only accessible by admins)
    path('api/v2/testimonials/delete/<int:pk>', TestimonialDeleteView.as_view(), name='testimonial-delete'),
]
