from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Applicant
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'app/Dashboard.html'


class ScholarshipsPageView(TemplateView):
    template_name = 'app/Scholarships.html'


class ApplicantListView(ListView):
    model = Applicant
    context_object_name = 'applicants'
    template_name = 'app/applicant_list.html'


class ApplicantDetailView(DetailView):
    model = Applicant
    context_object_name = 'applicant'
    template_name = 'app/applicant_detail.html'


class ApplicantCreateView(CreateView):
    model = Applicant
    fields = ['first_name', 'last_name', 'birthdate', 'address', 'contact_no', 'email']
    template_name = 'app/applicant_create.html'
    success_url = reverse_lazy('applicant_list')


class ApplicantUpdateView(UpdateView):
    model = Applicant
    fields = ['first_name', 'last_name', 'birthdate', 'address', 'contact_no', 'email']
    template_name = 'app/applicant_update.html'
    success_url = reverse_lazy('applicant_list')


class ApplicantDeleteView(DeleteView):
    model = Applicant
    template_name = 'app/applicant_delete.html'
    success_url = reverse_lazy('applicant_list')


class RequirementsPageView(TemplateView):
    template_name = 'app/Requirements.html'


class AnnouncementsPageView(TemplateView):
    template_name = 'app/Announcements.html'


class ContactPageView(TemplateView):
    template_name = 'app/Contact.html'