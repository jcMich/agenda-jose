from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
from agenda.forms import ContactoForm
from agenda.models import Contactos


def index(request):
    return render_to_response('agenda/index.html', {'contactos': Contactos.objects.all()})


def add_contact(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            ps = form.save(commit=False)
            ps.save()
            form.save_m2m()
            return render_to_response('agenda/index.html', {'contactos': Contactos.objects.all()},
                                      context_instance=RequestContext(request))
        return render_to_response('agenda/addContact.html', {'form': form}, context_instance=RequestContext(request))
    elif request.method == "GET":
        form = ContactoForm()
        ctx = {'msg': "hola mundo", 'form': form}
        return render_to_response('agenda/addContact.html', ctx, context_instance=RequestContext(request))


def contact_detail(request, pk):
    contact = Contactos.objects.get(pk=pk)
    return render_to_response('contact_detail.html', {'contacto': contact}, context_instance=RequestContext(request))
