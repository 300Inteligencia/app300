from ..models import Cliente

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone, endereco=cliente.endereco, cpf=cliente.cpf, data_nascimento=cliente.data_nascimento, profissao=cliente.profissao, medico=cliente.medico)

def listar_clientes():
    return Cliente.objects.all().order_by('nome')

def listar_cliente_id(id):
    return Cliente.objects.get(id=id)

def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.email = cliente_novo.email
    cliente.endereco = cliente_novo.endereco
    cliente.telefone = cliente_novo.telefone
    cliente.cpf = cliente_novo.cpf
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.profissao = cliente_novo.profissao
    cliente.medico = cliente_novo.medico
    cliente.save(force_update=True)

def remover_cliente(cliente):
    cliente.delete()
