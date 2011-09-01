from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'mecanografia.requisicao_copias.views.index', name='index'),
    url(r'^material/', 'mecanografia.requisicao_copias.views.material', name='material'),
    url(r'^cadastrar_material/', 'mecanografia.requisicao_copias.views.cadastrar_material', name='cadastrar_material'),
    url(r'^editar_material/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.editar_material', name='editar_material'),
    url(r'^excluir_material/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.excluir_material', name='excluir_material'),    
    url(r'^setor/', 'mecanografia.requisicao_copias.views.setor', name='setor'),
    url(r'^cadastrar_setor/', 'mecanografia.requisicao_copias.views.cadastrar_setor', name='cadastrar_setor'),
    url(r'^editar_setor/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.editar_setor', name='editar_setor'),
    url(r'^excluir_setor/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.excluir_setor', name='excluir_setor'),
    
    
    url(r'^vincular_setor/', 'mecanografia.requisicao_copias.views.vincular_setor', name='vincular_setor'),
    
        
    url(r'^servidor/', 'mecanografia.requisicao_copias.views.servidor', name='servidor'),
    url(r'^cadastrar_servidor/', 'mecanografia.requisicao_copias.views.cadastrar_servidor', name='cadastrar_servidor'),
    url(r'^editar_servidor/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.editar_servidor', name='editar_servidor'),
    url(r'^excluir_servidor/(?P<codigo>\d+)', 'mecanografia.requisicao_copias.views.excluir_servidor', name='excluir_servidor'),    
    url(r'^media/(.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/login'}),
)
