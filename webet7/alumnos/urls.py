from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index, name='index'), #defino la URL de la app Alumnos
    path('alumnos/', views.alumnos, name='alumnos'),
    path('cursos', views.cursos, name='cursos'),
    path('docentes', views.docentes, name='docentes'),    
    path('novedades', views.novedades, name='novedades'),    
    path('tramites', views.tramites, name='tramites'),





#CODIGO DE LAS CLASES
    # path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
    # path('alumnos/detalle/<str:nombre_alumno>', views.alumno_detalle, name='alumnos_detalle'),
    # re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$',views.alumnos_historico, name='alumnos_historico'),
    # path('alumnos/activos', views.alumnos_estado, {'estado': 'activo'}, name='alumnos_activos'),
    # path('alumnos/inactivos', views.alumnos_estado, {'estado': 'inactivo'}, name='alumnos_inactivos'),
]