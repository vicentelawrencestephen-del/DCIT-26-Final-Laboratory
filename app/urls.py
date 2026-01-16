from django.urls import path
from .views import (
    HomePageView,
    RequirementsPageView,
    ScholarshipsPageView,
    AnnouncementsPageView,
    ContactPageView,
    ApplicantListView,
    ApplicantDetailView,
    ApplicantCreateView,
    ApplicantUpdateView,
    ApplicantDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('Scholarships/', ScholarshipsPageView.as_view(), name='Scholarships'),

    # Applicant URLs
    path('applicants/', ApplicantListView.as_view(), name='applicant_list'),
    path('applicant/<int:pk>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('applicant/create/', ApplicantCreateView.as_view(), name='applicant_create'),
    path('applicant/<int:pk>/edit/', ApplicantUpdateView.as_view(), name='applicant_update'),
    path('applicant/<int:pk>/delete/', ApplicantDeleteView.as_view(), name='applicant_delete'),

    path('Requirements/', RequirementsPageView.as_view(), name='Requirements'),
    path('Announcements/', AnnouncementsPageView.as_view(), name='Announcements'),
    path('Contact/', ContactPageView.as_view(), name='Contact'),
]