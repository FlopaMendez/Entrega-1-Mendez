from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import BuscarClienteForm, BuscarEmpleadoForm, ClienteForm, EmpleadoForm, HorasForm

from familia.models import Cliente, Empleado, HorasCliente


# --------VIEWS HOME:

def ir_a_home(request):
    template = loader.get_template('home_v2.html')
    context = {}
    return HttpResponse(template.render(context, request))


# --------VIEWS EMPLEADOS:

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

            return HttpResponseRedirect("/empleados")

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
        return HttpResponseRedirect("/empleados")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")



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
    


# --------VIEWS CLIENTES:

def ir_a_clientes(request):
    clientes = Cliente.objects.all()
    template = loader.get_template('clientes/lista_clientes.html')
    context = {
        'clientes': clientes,
    }
    return HttpResponse(template.render(context, request))


def agregar_cliente(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():

            nombre_empresa = form.cleaned_data['nombre_empresa']
            cuit_empresa = form.cleaned_data['cuit_empresa']
            nombre_contacto = form.cleaned_data['nombre_contacto']
            cargo_contacto = form.cleaned_data['cargo_contacto']
            cobro_mensual_honorarios = form.cleaned_data['cobro_mensual_honorarios']
            Cliente(nombre_empresa=nombre_empresa, cuit_empresa=cuit_empresa, nombre_contacto=nombre_contacto, cargo_contacto=cargo_contacto, cobro_mensual_honorarios=cobro_mensual_honorarios).save()

            return HttpResponseRedirect("/clientes")

    elif request.method == "GET":
        form = ClienteForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'clientes/form_carga_clientes.html', {'form': form})



def borrar_cliente(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        cliente = Cliente.objects.filter(id=int(identificador)).first()
        if cliente:
            cliente.delete()
        return HttpResponseRedirect("/clientes")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")



def buscar_cliente(request):
    if request.method == "GET":
        form_busqueda = BuscarClienteForm()
        return render(request, 'clientes/form_busqueda_cliente.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarClienteForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            clientes = Cliente.objects.filter(nombre_empresa__icontains=palabra_a_buscar)

        return  render(request, 'clientes/lista_clientes.html', {"clientes": clientes})


# --------VIEWS HORAS TRABAJADAS:

def ir_a_horas(request):
    horas_clientes = HorasCliente.objects.all()
    template = loader.get_template('horas_clientes/lista_horas_clientes.html')
    context = {
        'horas_clientes': horas_clientes,
    }
    return HttpResponse(template.render(context, request))



def agregar_horas(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = HorasForm(request.POST)
        if form.is_valid():

            nombre_cliente = form.cleaned_data['nombre_cliente']
            fecha_de_trabajo = form.cleaned_data['fecha_de_trabajo']
            horas_trabajadas = form.cleaned_data['horas_trabajadas']
            HorasCliente(nombre_cliente=nombre_cliente, fecha_de_trabajo=fecha_de_trabajo, horas_trabajadas=horas_trabajadas).save()

            return HttpResponseRedirect("/horas_clientes")

    elif request.method == "GET":
        form = HorasForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'horas_clientes/form_carga_horas.html', {'form': form})


def borrar_horas(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        horas_cliente = HorasCliente.objects.filter(id=int(identificador)).first()
        if horas_cliente:
            horas_cliente.delete()
        return HttpResponseRedirect("/horas_clientes")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")