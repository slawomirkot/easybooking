from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View


from bookingvisit.models import Client_Profil, Reservation_Hairdresser, Reservation_Beautician, Opinions


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class ClientProfilView(DetailView):
    model = Client_Profil
    template_name = 'client_profil.html'


class UserNameUpdateView(UpdateView):
    model = User
    template_name = 'client_update.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class UserEmailUpdateView(UpdateView):
    model = User
    template_name = 'client_update.html'
    fields = ['email']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class UpdateClientProfilView(UpdateView):
    model = Client_Profil
    template_name = 'client_update.html'
    fields = ['phone_number']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class ReservationHairdersesrView(CreateView):
    model = Reservation_Hairdresser
    template_name = 'client_reservation.html'
    fields = ['employees', 'services', 'day', 'start_time']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class ReservationBeauticianView(CreateView):
    model = Reservation_Beautician
    template_name = 'client_reservation.html'
    fields = ['employees', 'services', 'day', 'start_time']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class ReservationListView(ListView):
    model = Client_Profil
    template_name = 'client_reservation_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReservationListView, self).get_context_data(**kwargs)
        context = {
            'rezervation_list':Reservation_Beautician.objects.filter(client=self.kwargs.get('pk')),
            'rezervation_list_2':Reservation_Hairdresser.objects.filter(client=self.kwargs.get('pk')),
        }
        return context

class ClientOpinonView(CreateView):
    model = Opinions
    template_name = 'client_update.html'
    fields = ['rating', 'opinion']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class ClientOpinonUpdateView(UpdateView):
    model = Opinions
    template_name = 'client_update.html'
    fields = ['rating', 'opinion']
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_object_or_404(Opinions, client=self.kwargs.get('pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class ClientOpinonDeleteView(DeleteView):
    model = Opinions
    template_name = 'client_delete_opinion.html'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_object_or_404(Opinions, client=self.kwargs.get('pk'))

class ClientOpinionListView(ListView):
    model = Client_Profil
    template_name = 'client_opinion.html'

    def get_context_data(self, **kwargs):
        context = super(ClientOpinionListView, self).get_context_data(**kwargs)
        context['opinion_list'] = Opinions.objects.filter(client=self.kwargs.get('pk'))
        return context

class OpinionsListView(ListView):
    model = Opinions
    template_name = 'opinion.html'

    def get(self, request):
        opinions_list = Opinions.objects.all()
        context={
            'opinions_list': opinions_list
        }
        return render(request, 'opinion.html', context)