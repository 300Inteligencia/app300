from django.urls import path
from .views import cliente_views, orcamento_views, funcionario_views, autenticacao_views

urlpatterns = [
    path('cadastrar_cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes', cliente_views.listar_clientes, name='listar_clientes'),
    path('lista_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('editar_orcamento/<int:id>', orcamento_views.editar_orcamento, name='editar_orcamento'),
    path('remover_cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
    path('remover_orcamento/<int:id>', orcamento_views.remover_orcamento, name='remover_orcamento'),
    path('cadastrar_orcamento/<int:id>', orcamento_views.inserir_orcamento, name='cadastrar_orcamento'),
    path('lista_orcamentos/<int:id>', orcamento_views.listar_orcamento_id, name='listar_orcamento_id'),
    path('cadastrar_funcionario', funcionario_views.inserir_funcionario, name='cadastrar_funcionario'),
    path('listar_funcionarios', funcionario_views.listar_funcionarios, name='listar_funcionarios'),
    path('login', autenticacao_views.login_usuario, name='login'),
    path('logout', autenticacao_views.deslogar_usuario, name='logout'),
    path('enviar_orcamento/<int:id>', orcamento_views.enviar_email_orcamento, name='enviar_orcamento'),
    path('orcamentos/contagem/', orcamento_views.contagem_orcamentos, name='contagem_todos_orcamentos'),
    path('remover_funcionario/<int:id>', funcionario_views.remover_funcionario, name='remover_funcionario')
    ]