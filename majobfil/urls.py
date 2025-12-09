from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lojas import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("conta.urls")),
    path('balanco/', include("balanco.urls")),
    path('loja/', include("lojas.urls")),
    path('relatorio/', include("relatorio.urls")),
    path('produtos/', include("produtos.urls")),
    path('api/totais-vendas/', views.api_totais_vendas, name='api_totais_vendas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)