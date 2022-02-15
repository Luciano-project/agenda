from django.db import models
#** Esta importação vai nos permitir a criação de usuários com sua agenda e compromissos prórpios
from django.contrib.auth.models import User

# Create your models here.
#Esta classe, a seguir, será responsável pela maniulação dos dados que serão inseridos logo mais na aplicação
class Evento(models.Model):
    #Aqui teremos as confirgurações das informações que serão inseridas nos bancos de dados:
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao= models.DateTimeField(auto_now=True)
    #** Aqui trazemos a importação do usuário. Definimos que ao excluir, tudo relacionado a ele também se vai
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

# Depois de fazer a migração será criada uma tabela padrão com o nome "core_eventos"
#para que possamos alterar a mesma façamos:
    class Meta:
        db_table = 'evento'

# Aqui definimos como o django vai representar como nome das tabelas na página do Django Admin
    def __str__(self):
        return self.titulo