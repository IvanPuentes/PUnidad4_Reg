from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
import stripe
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission
from mipagina.models import Vuelo,Viaje,Hospedaje
from django.core.mail import send_mail
from django.conf import settings
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


#view de de la compra de vuelos con correo para confirmacion
class OrdersPageView(DetailView):
    model = Vuelo
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descripcion','escala','precio','img',
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    

    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        ciudad = request.POST["ciudad"]
        sub = "Registro de pago de Vuelo" 
        message = "Gracias por realizar el pago del Vuelo con destino a "+ ciudad +" "+ "por la cantidad de "+ cantidad
        email_from="ivan.puentes2525@gmail.com"
        recipent_list=[request.POST["email"]]

        send_mail(sub,message,email_from,recipent_list)
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')


#view de de la compra de viajes con correo para confirmacion
class OrdersViajePageView(DetailView):
    model = Viaje
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descripcion','precio','img','noches',
    template_name = 'orders/purchaseViaje.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
     
    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        ciudad = request.POST["ciudad"]
        sub = "Registro de pago de Viaje" 
        message = "Gracias por realizar el pago del Viaje con destino a "+ ciudad +" "+ "por la cantidad de "+ cantidad
        email_from="ivan.puentes2525@gmail.com"
        recipent_list=[request.POST["email"]]

        send_mail(sub,message,email_from,recipent_list)
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')

#view de de la compra de hospedajes con correo para confirmacion        
class OrdersHospPageView(DetailView):
    model = Hospedaje
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descripcion','precio','img','noches',
    template_name = 'orders/purchaseHops.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
     
    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        ciudad = request.POST["ciudad"]
        sub = "Registro de pago de Hospedaje" 
        message = "Gracias por realizar el pago del Hospedaje con destino a "+ ciudad +" "+ "por la cantidad de "+ cantidad
        email_from="ivan.puentes2525@gmail.com"
        recipent_list=[request.POST["email"]]

        send_mail(sub,message,email_from,recipent_list)
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')

      