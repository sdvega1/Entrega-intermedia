from django.shortcuts import render, HttpResponse
from appVega.models import Jugador, Equipo

# Create your views here.
def inicio(request):

    jugadores = Jugador.objects.all()
  

  #    jugadores =  Jugador(nombre="Lionel Messi", nacionalidad="Argentino", edad=35)
   #   jugadores.save()
  #  documentoDeTexto = f"--->Nombre: {jugadores.nombre}   Nacionalidad: {jugadores.nacionalidad}  Edad: {jugadores.edad}"



    return render(request, 'inicio.html', {'jugadores':jugadores})
 
    equipos = Equipo.objects.all()
    return render(request, 'inicio.html', {'equipos':equipos})


