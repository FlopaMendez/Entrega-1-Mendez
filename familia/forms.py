from django import forms

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    dni = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "sin puntos ni espacios"}))

class BuscarEmpleadoForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")