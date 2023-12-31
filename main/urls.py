"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from reservas.views import ErroView, IndexView,ReservaListView, DetalheReservaView, CadastroView, EditarCadastroView,ExcluirCadastroView
from stand.views import StandListView, DetalheStandView, CreateStandView, EditarStandView,ExcluirStandView
# from admin_view.views import AdminHomeView, AdminLoginview

urlpatterns = [
    # general
    path('admin/', admin.site.urls), 
    path('accounts/', include('allauth.urls')),

    # reservas
    path('', IndexView.as_view(), name='index'),   
    path('reserva/', ReservaListView.as_view() ,name='lista_reserva'),
    path('reserva/cadastro/', CadastroView.as_view(), name='cadastro'),
    path('reserva/<int:pk>',DetalheReservaView.as_view(), name='reserva'),
    path('reserva/editarreserva/<int:pk>', EditarCadastroView.as_view(),name='editar'),
    path('reserva/excluirreserva/<int:pk>', ExcluirCadastroView.as_view(),name='excluir'),
    path('reserva/erro/', ErroView.as_view(), name='erro'),

    # stands
    path('stand/',StandListView.as_view(),name='lista_stand'),
    path('stand/cadastro/', CreateStandView.as_view(), name='stand_form'),
    path('stand/<int:pk>',DetalheStandView.as_view(), name='stand'),
    path('stand/editarreserva/<int:pk>', EditarStandView.as_view(),name='editar_stand'),
    path('stand/excluirreserva/<int:pk>', ExcluirStandView.as_view(),name='excluir_stand'),

    # Account
    

    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
