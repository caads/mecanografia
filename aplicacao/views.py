# coding: utf-8 

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from ddiex_social.aplicacao.models import Bolsa, BolsaForm, Edital, EditalForm, Setor, SetorForm, Inscricao, InscricaoForm, Bolsista, BolsistaForm, AjudaCusto, AjudaCustoForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, get_connection, EmailMessage
#from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch
import os
from django.core.urlresolvers import reverse
from cStringIO import StringIO
#from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, A4
#from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
#from reportlab.lib.styles import getSampleStyleSheet
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
import mimetypes, os



#pagina principal
def index(request):
    edital = Edital.objects.all()
    return render_to_response('index.html', {'edital':edital, 'user':request.user})
   

#cadastro de bolsa
@login_required
def cadastrar_bolsa(request):
    if request.POST:
        f = BolsaForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Bolsa cadastrada com sucesso.'
            formulario = 'Cadastro de Bolsa'
            voltar = '/bolsa/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response('cadastrar_bolsa.html', {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = BolsaForm()
        return render_to_response('cadastrar_bolsa.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de bolsa
@login_required
def bolsa(request):
    consulta = Bolsa.objects.all().order_by('modalidade')
    return render_to_response('bolsa.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
@login_required
def editar_bolsa(request, codigo):
    bolsa = get_object_or_404(Bolsa, pk = codigo)
    f = BolsaForm(request.POST, instance = bolsa)
    if request.POST:
        if f.is_valid():
            bolsa = f.save()
            mensagem = 'Bolsa alterada com sucesso.'
            formulario = 'Editar Bolsa'
            voltar = '/bolsa/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response("editar_bolsa.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        codigo = bolsa.id
        f = BolsaForm(instance=bolsa)
        return render_to_response('editar_bolsa.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir bolsa
@login_required
def excluir_bolsa(request, codigo):
    bolsa = get_object_or_404(Bolsa, pk=codigo)
    bolsa.delete()
    mensagem = 'Bolsa excluída com sucesso.'
    formulario = 'Excluir Bolsa'
    voltar = '/bolsa/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})




#cadastro de bolsa
@login_required
def cadastrar_setor(request):
    if request.POST:
        f = SetorForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Setor cadastrado com sucesso.'
            formulario = 'Cadastro de setor'
            voltar = '/setor/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response('cadastrar_setor.html', {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = SetorForm()
        return render_to_response('cadastrar_setor.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de bolsa
@login_required
def setor(request):
    consulta = Setor.objects.all().order_by('descricao')
    return render_to_response('setor.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
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
            return render_to_response("editar_setor.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        codigo = setor.id
        f = SetorForm(instance=setor)
        return render_to_response('editar_setor.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir bolsa
@login_required
def excluir_setor(request, codigo):
    setor = get_object_or_404(Setor, pk=codigo)
    setor.delete()
    mensagem = 'Setor excluído com sucesso.'
    formulario = 'Excluir Setor'
    voltar = '/setor/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})    
    




#cadastro de bolsa
@login_required
def cadastrar_ajuda_custo(request):
    if request.POST:
        f = AjudaCustoForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Ajuda de Custo cadastrado com sucesso.'
            formulario = 'Cadastro de Ajuda de Custo'
            voltar = '/ajuda_custo/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response('cadastrar_ajuda_custo.html', {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = AjudaCustoForm()
        return render_to_response('cadastrar_ajuda_custo.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de bolsa
@login_required
def ajuda_custo(request):
    consulta = AjudaCusto.objects.all().order_by('nome')
    return render_to_response('ajuda_custo.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
@login_required
def editar_ajuda_custo(request, codigo):
    ajuda_custo = get_object_or_404(AjudaCusto, pk = codigo)
    f = AjudaCustoForm(request.POST, instance = ajuda_custo)
    if request.POST:
        if f.is_valid():
            ajuda_custo = f.save()
            mensagem = 'Ajuda de Custo alterada com sucesso.'
            formulario = 'Editar Ajuda de Custo'
            voltar = '/ajuda_custo/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response("editar_ajuda_custo.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        codigo = ajuda_custo.id
        f = AjudaCustoForm(instance=ajuda_custo)
        return render_to_response('editar_ajuda_custo.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir bolsa
@login_required
def excluir_ajuda_custo(request, codigo):
    ajuda_custo = get_object_or_404(AjudaCusto, pk=codigo)
    ajuda_custo.delete()
    mensagem = 'Ajuda de custo excluída com sucesso.'
    formulario = 'Excluir Ajuda de custo'
    voltar = '/ajuda_custo/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})    
    
    
    
    
    
    
#cadastro de bolsa
@login_required
def cadastrar_bolsista(request):
    if request.POST:
        f = BolsistaForm(request.POST)
        if f.is_valid():
            f.save()
            mensagem = 'Bolsista cadastrado com sucesso.'
            formulario = 'Cadastro de Bolsista'
            voltar = '/bolsista/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response('bolsista.html', {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = BolsistaForm()
        return render_to_response('cadastrar_bolsista.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de bolsa
@login_required
def bolsista(request):
    consulta = Bolsista.objects.all().order_by('nome')
    return render_to_response('bolsista.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
@login_required
def editar_bolsista(request, codigo):
    bolsista = get_object_or_404(Bolsista, pk = codigo)
    f = BolsistaForm(request.POST, instance = bolsista)
    if request.POST:
        if f.is_valid():
            bolsista = f.save()
            mensagem = 'Bolsista alterado com sucesso.'
            formulario = 'Editar bolsista'
            voltar = '/bolsista/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response("editar_bolsista.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        codigo = bolsista.id
        f = BolsistaForm(instance=bolsista)
        return render_to_response('editar_bolsista.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir bolsa
@login_required
def excluir_bolsista(request, codigo):
    bolsista = get_object_or_404(Bolsista, pk=codigo)
    bolsista.delete()
    mensagem = 'Bolsista excluído com sucesso.'
    formulario = 'Excluir bolsista'
    voltar = '/bolsista/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})    
    

    
    
    
    
    
#cadastro de bolsa
@login_required
def cadastrar_edital(request):
    if request.POST:
        f = EditalForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            mensagem = 'Edital cadastrado com sucesso.'
            formulario = 'Cadastro de Edital'
            voltar = '/edital/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response('cadastrar_edital.html', {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = EditalForm()
        return render_to_response('cadastrar_edital.html', {'user':request.user, 'form':f})

#consulta e acesso aos dados de bolsa
@login_required
def edital(request):
    consulta = Edital.objects.all()
    return render_to_response('edital.html', {'user':request.user, 'consulta': consulta})

#alteração de dados de materiais
@login_required
def editar_edital(request, codigo):
    edital = get_object_or_404(Edital, pk = codigo)
    f = EditalForm(request.POST, request.FILES, instance = edital)
    if request.POST:
        if f.is_valid():
            edital = f.save()
            mensagem = 'Edital alterado com sucesso.'
            formulario = 'Editar Edital'
            voltar = '/edital/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response("editar_edital.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        codigo = edital.id
        f = EditalForm(instance=edital)
        return render_to_response('editar_edital.html', {'form':f, 'codigo':codigo, 'user':request.user})

#excluir bolsa
@login_required
def excluir_edital(request, codigo):
    edital = get_object_or_404(Edital, pk=codigo)
    edital.delete()
    mensagem = 'Edital excluído com sucesso.'
    formulario = 'Excluir edital'
    voltar = '/edital/'
    return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})    
        
    
    
def inscricao(request, codigo):
    #inscricao = get_object_or_404(Bolsa, pk = codigo)    
    if request.POST:
        f = InscricaoForm(request.POST)
        if f.is_valid():
            inscricao = f.save()
            mensagem = 'Inscrição realizada com sucesso. \n Número da Inscrição: '+ str(inscricao.id)
            formulario = 'Inscrição'
            voltar = '/'
            return render_to_response('sucesso.html', {'user':request.user, 'mensagem':mensagem, 'link':voltar, 'formulario':formulario})
        else:
            erro = True
            return render_to_response("inscricao.html", {'user':request.user, 'form':f, 'erro': erro})
    else:
        f = InscricaoForm()
        return render_to_response('inscricao.html', {'form':f, 'codigo':codigo, 'user':request.user})    
        
        
        
def relatorio(request):
    edital = Edital.objects.all().order_by("numero_edital")
    if request.POST:
        if request.POST['status'] == 'bolsista':
            relatorio = Bolsista.objects.all().order_by('nome')
            return render_to_response('relatorio_bolsista.html', {'user':request.user, 'relatorio':relatorio}) 
    
        elif request.POST['status'] == 'inscritos':
            relatorio = Inscricao.objects.filter(edital = request.POST['edital']).order_by('nome')
            return render_to_response('inscritos.html', {'user':request.user, 'relatorio':relatorio}) 
        else:
            erro = True
            return render_to_response('relatorio.html', {'user':request.user, 'edital':edital}) 
    else:
        return render_to_response('relatorio.html', {'user':request.user, 'edital':edital})
    

