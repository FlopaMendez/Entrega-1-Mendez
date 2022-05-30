from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import BuscarEmpleadoForm, EmpleadoForm

from familia.models import Clientes, Empleado

def ir_a_home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def ir_a_empleados(request):
    empleados = Empleado.objects.all()
    template = loader.get_template('empleados/lista_empleados.html')
    context = {
        'empleados': empleados,
    }
    return HttpResponse(template.render(context, request))


def agregar_empleado(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            dni = form.cleaned_data['dni']
            Empleado(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, dni=dni).save()

            return HttpResponseRedirect("/")

    elif request.method == "GET":
        form = EmpleadoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'empleados/form_carga.html', {'form': form})


def borrar_empleado(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        empleado = Empleado.objects.filter(id=int(identificador)).first()
        if empleado:
            empleado.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


# def actualizar(request, identificador):
#     '''
#     TODO: implementar una vista para actualización
#     '''
#     pass


def buscar_empleado(request):
    if request.method == "GET":
        form_busqueda = BuscarEmpleadoForm()
        return render(request, 'empleados/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarEmpleadoForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            empleados = Empleado.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'empleados/lista_empleados.html', {"empleados": empleados})
    



def ir_a_clientes(request):
    clientes = Clientes.objects.all()
    template = loader.get_template('clientes/lista_clientes.html')
    context = {
        'clientes': clientes,
    }
    return HttpResponse(template.render(context, request))
