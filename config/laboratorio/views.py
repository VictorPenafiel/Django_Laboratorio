from django.shortcuts import render, redirect
from .models import Laboratorio

# Create your views here.
# Controladores-vistas para CRUD
def insertar_lab(request):
    if request.method == "POST":
        nombre = request.POST['lab_nombre']
        ciudad = request.POST['lab_ciudad']
        pais = request.POST['lab_pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('mostrar-lab/')
    else:
        return render(request, 'insertar-lab.html')

# obtener los Laboratorios
def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'laboratorios':laboratorios,
        'num_visits': num_visits,
    }
    print(laboratorios.values())
    return render(request,'mostrar-lab.html', context)
# Editar Laboratorio
def editar_lab(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    # if request.method == 'POST':
    # return redirect('/crudapp/mostrar')
    context = {
        'laboratorio': laboratorio,
    }
    return render(request=request, template_name='editar-emp.html', context=context)
def actualizar_laboratorio(request, id):
    lab_nombre = request.POST['lab_nombre']
    lab_ciudad = request.POST['lab_ciudad']
    lab_pais = request.POST['lab_pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre= lab_nombre
    laboratorio.ciudad = lab_ciudad
    laboratorio.pais = lab_pais
    laboratorio.save()
    return redirect('/laboratorio/mostrar-lab')

# Eliminar Laboratorio
def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST': laboratorio.delete()
    return redirect('/laboratorio/mostrar-lab')
    context = {
        'laboratorio': laboratorio,
    }
    return render(request, 'eliminar-lab.html', context)