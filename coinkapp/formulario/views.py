from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic
from django import forms

from .models import User
from .forms import FormularioUsuarios

class FormularioUserView(HttpRequest):
    
    """_summary_
    """
    def index(request):
        """_summary_

        Args:
            request (_type_): _description_
            The user variable is created by importing the data from FormularioUsuarios

        Returns:
            _type_: _description_
            returns a view of the render 
        """
        usuario= FormularioUsuarios()
        return render(request,"formulario/UserIndex.html",{
            "form": usuario
        })
    
    def procesar_formulario(request):
        """_summary_

        Args:
            request (_type_): _description_
            in order to save the information in the table, first we ask if the information is valid or not, 
            is_valid():, the method returns true, then it is saved in the database table.

        Returns:
            _type_: _description_
            the user variable is instantiated, then a view is returned, in this case it is for the same 
            view where the form is located so that the user can enter or not more data to the system.
        """
        usuario = FormularioUsuarios(request.POST) 
        print(usuario)      
        if usuario.is_valid():
            usuario.save()
            usuario = FormularioUsuarios()
        
        return render(request, "formulario/formulario.html",{
            "form": usuario, 
            "mensaje": "OK"
        })
        
    def UserList(request):
        listas = User.objects.all()
        return render(request,"formulario/UserList.html",{
            "users": listas
            },)
        