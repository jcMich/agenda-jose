from django.shortcuts import render_to_response, render
from django.template import RequestContext

# Create your views here.
from agenda.forms import ContactoForm, GroupForm, ColorForm
from agenda.models import Contactos, Grupos, Colores


def index(request):
    return render_to_response('agenda/index.html', {'contactos': Contactos.objects.all(),'grupos': Grupos.objects.all(), 'colores': Colores.objects.all()})


def add_contact(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            ps = form.save(commit=False)
            ps.save()
            form.save_m2m()
            return render_to_response('agenda/index.html', {'contactos': Contactos.objects.all(), 'grupos': Grupos.objects.all(),'colores': Colores.objects.all()},                   context_instance=RequestContext(request))
        return render_to_response('agenda/addContact.html', {'form': form}, context_instance=RequestContext(request))
    elif request.method == "GET":
        form = ContactoForm()
        ctx = {'msg': "hola mundo", 'form': form}
        return render_to_response('agenda/addContact.html', ctx, context_instance=RequestContext(request))


def contact_detail(request, pk):
    contact = Contactos.objects.get(pk=pk)
    return render_to_response('contact_detail.html', {'contacto': contact}, context_instance=RequestContext(request))


def add_group(request):
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('agenda/index.html', {'grupos': Grupos.objects.all(), 'contactos': Contactos.objects.all(),'colores': Colores.objects.all()},				context_instance=RequestContext(request))
	 	return render_to_response('agenda/addContact.html', {'form': form}, context_instance=RequestContext(request))
	elif request.method == "GET":
        	form = GroupForm()
        	ctx = {'msg': "Agregar Grupo", 'form': form}
        	return render_to_response('agenda/addContact.html', ctx, context_instance=RequestContext(request))


def group_detail(request, pk):
    grupo = Grupos.objects.get(pk=pk)
    return render(request,'group_detail.html', {'grupo': grupo})

def delete(request):
	grupo = Grupos.objects.all()	
	return render(request,'show_delete.html',{'grupo': grupo})

def delete_group(request,pk):
	d = Grupos.objects.get(pk=pk)
	d.delete()
	grupo = Grupos.objects.all()
	return render(request,'show_delete.html',{'grupo': grupo})
	
###################################

def add_color(request):
	if request.method == 'POST':
		form = ColorForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('agenda/index.html', {'grupos': Grupos.objects.all(), 'contactos': Contactos.objects.all(),'colores': Colores.objects.all()},						context_instance=RequestContext(request))
	 	return render_to_response('agenda/addContact.html', {'form': form}, context_instance=RequestContext(request))
	elif request.method == "GET":
        	form = ColorForm()
        	ctx = {'msg': "Agregar Color", 'form': form}
        	return render_to_response('agenda/addContact.html', ctx, context_instance=RequestContext(request))


def color_detail(request, pk):
    color = Colores.objects.get(pk=pk)
    return render(request,'color_detail.html', {'colores': color})

	

