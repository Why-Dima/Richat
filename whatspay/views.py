import stripe
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'whatspay/success.html'


class CancelView(TemplateView):
    template_name = 'whatspay/cancel.html'


class ProductView(TemplateView):
    template_name = 'whatspay/index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.all()
        context = super(ProductView, self).get_context_data(**kwargs)
        context.update({
            'product': item,
        })
        return context


class CeckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Item.objects.get(id=product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(    
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': 1,
            }],
            mode='payment',          
            success_url='http://127.0.0.1:8000/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(session.url, code=303)

