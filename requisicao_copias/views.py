# coding: utf-8 

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from mecanografia.requisicao_copias.models import Materiais, MateriaisForm, Setor, SetorForm, Servidor, ServidorForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, get_connection, EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from django.core.urlresolvers import reverse
from cStringIO import StringIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction


#pagina principal
def index(request):
    return render_to_response('index.html', {'user':request.user})

#cadastro de material
@login_required
def cadastrar_material(request):
    if request.POST:
        f = MateriaisForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Material cadastrado com sucesso.'
            formulario = 'Cadastro de Material'
            voltar = '/material/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response('cadastrar_material.html', {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        f = MateriaisForm()
        return render_to_response('cadastrar_material.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de materiais
@login_required
def material(request):
    consulta = Materiais.objects.all().order_by('descricao')
    return render_to_response('material.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
@login_required
def editar_material(request, codigo):
    material = get_object_or_404(Materiais, pk = codigo)
    f = MateriaisForm(request.POST, instance = material)
    if request.POST:
        if f.is_valid():
            material = f.save()
            mensagem = 'Material alterado com sucesso.'
            formulario = 'Editar Material'
            voltar = '/material/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response("editar_material.html", {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        codigo = material.id
        f = MateriaisForm(instance=material)
        return render_to_response('editar_material.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir material
@login_required
def excluir_material(request, codigo):
    material = get_object_or_404(Materiais, pk=codigo)
    material.delete()
    mensagem = 'Material excluído com sucesso.'
    formulario = 'Editar Material'
    voltar = '/material/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
    
    
#cadastro de setor
@login_required
def cadastrar_setor(request):
    if request.POST:
        f = SetorForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Setor cadastrado com sucesso.'
            formulario = 'Cadastro de Setor'
            voltar = '/setor/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response('cadastrar_setor.html', {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        f = SetorForm()
        return render_to_response('cadastrar_setor.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de setor
@login_required
def setor(request):
    consulta = Setor.objects.all().order_by('descricao')
    return render_to_response('setor.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de setor
@login_required
def editar_setor(request, codigo):
    setor = get_object_or_404(Setor, pk = codigo)
    f = SetorForm(request.POST, instance = setor)
    if request.POST:
        if f.is_valid():
            setor = f.save()
            mensagem = 'Setor alterado com sucesso.'
            formulario = 'Editar Setor'
            voltar = '/setor/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response("editar_setor.html", {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        codigo = setor.id
        f = SetorForm(instance=setor)
        return render_to_response('editar_setor.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir setor
@login_required
def excluir_setor(request, codigo):
    setor = get_object_or_404(Setor, pk=codigo)
    setor.delete()
    mensagem = 'Setor excluído com sucesso.'
    formulario = 'Editar Setor'
    voltar = '/setor/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
    
    
#cadastro de servidor
@login_required
def cadastrar_servidor(request):
    if request.POST:
        f = ServidorForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Servidor cadastrado com sucesso.'
            formulario = 'Cadastro de Servidor'
            voltar = '/servidor/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response('cadastrar_servidor.html', {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        f = ServidorForm()
        return render_to_response('cadastrar_servidor.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de servidor
@login_required
def servidor(request):
    if request.POST:
        if request.POST['status'] == 'siape':  
            consulta = Servidor.objects.filter(siape = request.POST['siape']).order_by('nome')
            contador = consulta.count()
            mensagem = ""
        elif request.POST['status'] == 'nome':
            consulta = Servidor.objects.filter(nome__icontains = request.POST['nome']).order_by('nome')
            contador = consulta.count()
            mensagem = ""
        elif request.POST['status'] == 'todos':
            consulta = Servidor.objects.order_by('nome')
            contador = consulta.count()
            mensagem = ""
        elif request.POST['status'] == '':
            consulta = []
            contador = 0
            mensagem = "Selecione um filtro para buscar"
        return render_to_response('servidor.html', {'consulta':consulta, 'user':request.user, 'contador':contador, 'mensagem':mensagem})
            
    #mostra a pagina de consulta ao servidor
    else:
        return render_to_response('servidor.html', {'user':request.user})

#alteração de dados de servidor
@login_required
def editar_servidor(request, codigo):
    servidor = get_object_or_404(Servidor, pk = codigo)
    f = ServidorForm(request.POST, instance = servidor)
    if request.POST:
        if f.is_valid():
            servidor = f.save()
            mensagem = 'Servidor alterado com sucesso.'
            formulario = 'Editar Servidor'
            voltar = '/servidor/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            mensagem_erro = 'Campo Obrigatório'
            return render_to_response("editar_servidor.html", {'user':request.user, 'form':f, 'erro': erro, 'mensagem_erro':mensagem_erro})
    else:
        codigo = servidor.siape
        f = ServidorForm(instance=servidor)
        return render_to_response('editar_servidor.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir servidor
@login_required
def excluir_servidor(request, codigo):
    servidor = get_object_or_404(Servidor, pk=codigo)
    servidor.delete()
    mensagem = 'Servidor excluído com sucesso.'
    formulario = 'Editar Servidor'
    voltar = '/servidor/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
    
