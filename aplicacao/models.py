#coding: utf-8

from django.db import models
from django.forms import ModelForm, ChoiceField, RadioSelect
from django import forms
from django.db import connection, transaction
from ddiex_social.aplicacao.validacao import UploadFile


#modelos
class Bolsa(models.Model):
    modalidade = models.CharField("Modalidade", max_length=50)
    valor_auxilio = models.CharField("Valor do Auxílio", max_length=50)
    carga_horaria = models.CharField("Carga Horária", max_length=50)
    
    def __unicode__(self):
        return self.modalidade
        
    
class Edital(models.Model):
    numero_edital = models.CharField("Número", max_length=50)
    descricao = models.CharField("Descrição", max_length=50)
    bolsa = models.ForeignKey('Bolsa')
    data_publicacao = models.CharField("Data da Publicação", max_length=50)
    data_expiracao = models.CharField("Data de Expiração", max_length=50)
    inicio_inscricao = models.CharField("Início da Inscrição", max_length=50)
    fim_inscricao = models.CharField("Início da Inscrição", max_length=50)
    hora_inicio = models.CharField("Hora de Início da Inscrição", max_length=50)
    hora_fim = models.CharField("Hora de Término da Inscrição", max_length=50)
    arquivo = UploadFile(upload_to='site/editais', max_upload_size=10000000, blank=False)
    
    def __unicode__(self):
        return self.numero_edital
        
        
class Setor(models.Model):
    descricao = models.CharField("Descricao", max_length=50)
    
    def __unicode__(self):
        return self.descricao
        
    


class Inscricao(models.Model):
    matricula = models.CharField("matricula", max_length=50)
    edital = models.CharField("Edital", max_length=50)
    nome = models.CharField("Nome", max_length=50)
    documento_identificacao = models.CharField("RG", max_length=50)
    cpf = models.CharField("CPF", max_length=50)
    email = models.CharField("E-mail", max_length=50)
    telefone = models.CharField("Telefone", max_length=50)
    celular = models.CharField("Celular", max_length=50)
    
    def __unicode__(self):
        return self.id       


class Bolsista(models.Model):
    matricula = models.CharField("matricula", max_length=50)
    nome = models.CharField("Nome", max_length=50)
    documento_identificacao = models.CharField("Documento de Identificação", max_length=50)
    cpf = models.CharField("CPF", max_length=50)
    inicio_bolsa = models.CharField("Data de Início da Bolsa", max_length=50)
    termino_bolsa = models.CharField("Data de Término da Bolsa", max_length=50)
    setor = models.ForeignKey('Setor')
    Bolsa = models.ForeignKey('Bolsa')
    banco = models.CharField("Banco", max_length=50)
    agencia = models.CharField("Agencia", max_length=50)
    conta_corrente = models.CharField("Conta Corrente", max_length=50)
    email = models.CharField("E-mail", max_length=50)
    telefone = models.CharField("Telefone", max_length=50)
    celular = models.CharField("Celular", max_length=50)
    
    def __unicode__(self):
        return self.nome
        
        
class AjudaCusto(models.Model):
    matricula = models.CharField("matricula", max_length=50)
    nome = models.CharField("Nome", max_length=50)
    documento_identificacao = models.CharField("RG", max_length=50)
    cpf = models.CharField("CPF", max_length=50)
    valor = models.CharField("Valor", max_length=50)
    justificativa = models.CharField("Justificativa", max_length=50)
    
    def __unicode__(self):
        return self.id               
        
        
            

#Formularios
class BolsaForm(ModelForm):
    class Meta:
        model = Bolsa
        
        
        
class EditalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditalForm, self).__init__(*args, **kwargs)

        bolsa = ['bolsa']
        for b in bolsa:
            self.fields[b].widget = forms.Select(choices = self.consulta())
             
    def consulta(self):
        bolsa = Bolsa.objects.all()
        self.bolsa = [(0,'')]
        for b in bolsa:
            self.bolsa.append((b.id, b.modalidade))
        return self.bolsa
        
    class Meta:
        model = Edital
        

class SetorForm(ModelForm):
    class Meta:
        model = Setor

        

        
        
class InscricaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InscricaoForm, self).__init__(*args, **kwargs)

        
            
        edital = ['edital']
        for e in edital:
            self.fields[e].widget = forms.HiddenInput(attrs={'value':'{{codigo}}'})    
            
    def consulta(self, numero_edital):
        setor = SetorEdital.objects.filter(edital=numero_edital)
        for s in setor:
            self.setor.append((s.setor_id, s.descricao))
        return self.setor
            
    class Meta:
        model = Inscricao
        
        
class BolsistaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BolsistaForm, self).__init__(*args, **kwargs)
        
        bolsa = ['Bolsa']
        for b in bolsa:
            self.fields[b].widget = forms.Select(choices = self.consulta())
             
    def consulta(self):
        bolsa = Bolsa.objects.all()
        self.bolsa = [(0,'')]
        for b in bolsa:
            self.bolsa.append((b.id, b.modalidade))
        return self.bolsa
            
    class Meta:
        model = Bolsista
        
        
class AjudaCustoForm(ModelForm):
               
    class Meta:
        model = AjudaCusto
