#coding: utf-8

from django.db import models
from django.forms import ModelForm, ChoiceField, RadioSelect
from django import forms
from django.db import connection, transaction

#modelos
class Materiais(models.Model):
    descricao = models.CharField("Descrição", max_length=50)
    
    
    
class Setor(models.Model):
    descricao = models.CharField("Descrição", max_length=50)
    
    
    
class Servidor(models.Model):
    siape = models.CharField("SIAPE", max_length=10, primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    cpf = models.CharField("CPF", max_length=50)
    pis = models.CharField("PIS/PASEP", max_length=50, blank=True)
    rg = models.CharField("RG", max_length=50, blank=True)
    orgao_expedidor = models.CharField("Órgão Expedidor", max_length=50, blank=True)
    data_emissao = models.CharField("Data de Emissão", max_length=50, blank=True)
    logradouro = models.CharField("Logradouro", max_length=50, blank=True)
    numero = models.CharField("Número", max_length=50, blank=True)
    complemento = models.CharField("Complemento", max_length=50, blank=True)
    bairro = models.CharField("Bairro", max_length=50, blank=True)
    cidade = models.CharField("Cidade", max_length=50, blank=True)
    uf = models.CharField("UF", max_length=50, blank=True)
    cep = models.CharField("CEP", max_length=50, blank=True)
    telefone = models.CharField("Telefone", max_length=50, blank=True)
    celular = models.CharField("Celular", max_length=50, blank=True)
    email = models.EmailField("E-mail", max_length=50)
    
    

#Formularios
class MateriaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MateriaisForm, self).__init__(*args, **kwargs)

        descricao = ['descricao']
        for m in descricao:
            self.fields[m].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})

    class Meta:
        model = Materiais
        
        
        
class SetorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SetorForm, self).__init__(*args, **kwargs)

        descricao = ['descricao']
        for s in descricao:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})

    class Meta:
        model = Setor
        
        
        
class ServidorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServidorForm, self).__init__(*args, **kwargs)

        nome = ['nome']
        for s in nome:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
            
        orgao_expedidor = ['orgao_expedidor']
        for s in orgao_expedidor:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
        
        logradouro = ['logradouro']
        for s in logradouro:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
            
        complemento = ['complemento']
        for s in complemento:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
            
        bairro = ['bairro']
        for s in bairro:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
            
        cidade = ['cidade']
        for s in cidade:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'30'})
            
        uf = ['uf']
        for s in uf:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'maiuscula(this.value);', 'maxlength':'2'})

        email = ['email']
        for s in email:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'minuscula(this.value);', 'maxlength':'30'})
            
        siape = ['siape']
        for s in siape:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'num(this);', 'maxlength':'10'})
            
        cpf = ['cpf']
        for s in cpf:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'num(this);', 'maxlength':'11'})
            
        pis = ['pis']
        for s in pis:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'maxlength':'20'})
            
        rg = ['rg']
        for s in rg:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'num(this);', 'maxlength':'9'})
            
        numero = ['numero']
        for s in numero:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'onkeyup':'num(this);', 'maxlength':'5'})
            
        cep = ['cep']
        for s in cep:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40', 'maxlength':'8'})
            
        data_emissao = ['data_emissao']
        for s in data_emissao:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40'})
            
        telefone = ['telefone']
        for s in telefone:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40'})
            
        celular = ['celular']
        for s in celular:
            self.fields[s].widget=forms.TextInput(attrs={'size':'40'})
            
    class Meta:
        model = Servidor
