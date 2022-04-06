from django.http import HttpResponse
from django.shortcuts import render
from AppKeepCoding.models import *

def curso(self):
    curso = Curso(nombre= "SQL", camada="28002")
    curso.save()
    documentoDeTexto =f"Curso: {curso.nombre}, camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)
def profesor(self):
    profesor = Profesor(nombre= "David", apellido="Martin", email="david.martin@gmail.com",profesion="profesor")
    profesor.save()
    documentoDeTexto =f"Nombre: {profesor.nombre}, apellido: {profesor.apellido}, su profesion es: {profesor.profesion}"
    return HttpResponse(documentoDeTexto)
