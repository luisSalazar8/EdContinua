from django.urls import path
from django_filters.views import FilterView
from . import views

urlpatterns = [
	path("", views.index, name="pac_index"),
	path("nuevo/", views.PACCreate.as_view(), name="pac_nuevo"),
	path("editar/<pk>/", views.PACUpdate.as_view(), name="pac_editar"),
	path('ajax/load-elminar-pac',views.pac_conf_elim,name='pac_confirmar_eliminar'),
    path('eliminar/<pk>/', views.PACDelete.as_view(), name='pac_eliminar'),
	path('partida/nuevo/<pk>/',views.PartidaCreate.as_view(),name='partida_nuevo'),
	path('ajax/partida-update/',views.partida_update,name='partida_editar'),
	path('partida/editar/<pk>/<fk>',views.PartidaUpdate.as_view(),name='partida_editar'),
	path('ajax/partida-eliminar',views.partida_eliminar,name='partida_eliminar'),
	path('partida/eliminar/<pk>/<fk>/',views.PartidaDelete.as_view(),name='partida_eliminar'),
	path('ajax/load-partida',views.load_partida,name='ajax_load_partida'),
	path('ajax/load-producto',views.load_producto,name='ajax_load_producto'),
    path('aprobar/<pk>',views.PACAprobar.as_view(), name="pac_aprobar"),
]