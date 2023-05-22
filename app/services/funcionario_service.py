from ..models import Funcionario


def listar_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios

def listar_funcionarios_id(id):
    funcionario = Funcionario.objects.get(id=id)
    return funcionario

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, nascimento=funcionario.nascimento, cargo=funcionario.cargo, username=funcionario.username,password=funcionario.password)

def remover_funcionario(funcionario):
    funcionario.delete()