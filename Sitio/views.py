from django.shortcuts import render, redirect
from .models import Producto, Usuario, Contacto

# Create your views here.

def inicio(request):
    productos = Producto.objects.all()

    return render(request, 'inicio.html', {
        'productos': productos
    })

def inicio(request):
    productos = Producto.objects.all()

    return render(request, 'maquillaje.html', {
        'productos': productos
    })

def buscar(request):
    termino = request.GET.get('q', '')

    productos = Producto.objects.filter(
        nombre__icontains=termino
    )

    return render(request, 'buscar.html', {
        'productos': productos,
        'termino': termino
    })
from django.shortcuts import render

def contacto(request):
    mensaje_exito = None
    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        if nombre and correo and mensaje:
            Contacto.objects.create(
                nombre=nombre,
                correo=correo,
                mensaje=mensaje
            )
            mensaje_exito = "Mensaje enviado correctamente"
        else:
            error = "Todos los campos son obligatorios"

    return render(request, "contacto.html", {
        "mensaje_exito": mensaje_exito,
        "error": error
    })

def ayuda(request):
    return render(request, 'ayuda.html')

def registro(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        Usuario.objects.create(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña
        )

        return redirect('inicio')

    return render(request, 'registro.html')

def login_view(request):
    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        contraseña = request.POST.get("contraseña")

        try:
            usuario = Usuario.objects.get(nombre=nombre)

            if usuario.contraseña == contraseña:
                request.session["usuario_id"] = usuario.id
                request.session["usuario_nombre"] = usuario.nombre

                return redirect("maquillaje") 
            else:
                error = "Contraseña incorrecta"

        except Usuario.DoesNotExist:
            error = "El usuario no existe"

    return render(request, "login.html", {"error": error})

def recuperar(request):
        mensaje = None
        error = None

        if request.method == "POST":
            nombre = request.POST.get("nombre")
            correo = request.POST.get("correo")
            contraseña_actual = request.POST.get("contraseña_actual")
            nueva_contraseña = request.POST.get("nueva_contraseña")

            try:
                usuario = Usuario.objects.get(nombre=nombre, correo=correo)

                # validar contraseña actual
                if usuario.contraseña == contraseña_actual:
                    usuario.contraseña = nueva_contraseña
                    usuario.save()

                    mensaje = "Contraseña actualizada correctamente"
                else:
                    error = "La contraseña actual no es correcta"

            except Usuario.DoesNotExist:
                error = "Usuario no encontrado"

        return render(request, "recuperar.html", {
            "mensaje": mensaje,
            "error": error
        })

def mapa_sitio(request):
    return render(request, 'mapa_sitio.html')
