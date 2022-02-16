from django.contrib import admin
from core.models import Evento


# Register your models here.
# Com esta classe determinamos as descrições sobre o evento na página do Django Admin

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento','data_criacao')

    # Aqui podemos criar uma caixa de pesquisa (lateral) onde são exibidos de acordo
    #com nossas preferências. Podemos inserir como parâmetro referências como: 'titulo',
    #'usuario', 'data_evento', etc)
    list_filter = ('usuario','data_evento',) # Aqui podemos inserir outras referencias de acordo
    #com as varáveis existentes em nossas tabelas

# Este comando exibe a tabela na página do django admin
admin.site.register(Evento, EventoAdmin)

