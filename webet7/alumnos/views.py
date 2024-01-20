from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "alumnos/index.html")

def alumnos(request):
    return render(request, "alumnos/alumnos.html")

def cursos(request):
    return render(request, "cursos.html")

def docentes(request):
    return render(request, "docentes.html")

def novedades(request):
    return render(request, "novedades.html")

def tramites(request):
    return render(request, "tramites.html")





#CODIGO DE LAS CLASES

# def alumnos_listado(request):
#     return HttpResponse("""
#     <ul>
#         <li>Pepe Gonzalez</li>
#         <li>Jose Rodriguez</li>
#         <li>Maria del Cerro</li>
#     </ul>
# """)

# def alumno_detalle(request, nombre_alumno):
#     return HttpResponse(
#         f"""
#         <h1>Bienvenido {nombre_alumno} </h1>
#         <p>Pagina Personal de usuario</p>
#         """
#     )

# def alumnos_historico(request, year):
#     return HttpResponse(
#         f"<h1>HIstorico de Alumnos del año: {year}</h1>"
#     )

# def alumnos_estado(request, estado):
#     return HttpResponse  (f"Filtrar alumnos por: {estado}")
