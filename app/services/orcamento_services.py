from ..models import Orcamento

def cadastrar_orcamento(orcamento):
    orc_bd = Orcamento.objects.create(
        nomeorc = orcamento.nomeorc,
        descr = orcamento.descr,
        proc1 = orcamento.proc1, 
        val1 = orcamento.val1, 
        pag1 = orcamento.pag1,
        proc2 = orcamento.proc2, 
        val2 = orcamento.val2, 
        pag2 = orcamento.pag2,
        proc3 = orcamento.proc3, 
        val3 = orcamento.val3, 
        pag3 = orcamento.pag3,
        proc4 = orcamento.proc4, 
        val4 = orcamento.val4, 
        pag4 = orcamento.pag4,
        proc5 = orcamento.proc5, 
        val5 = orcamento.val5, 
        pag5 = orcamento.pag5,
        proc6 = orcamento.proc6, 
        val6 = orcamento.val6, 
        pag6 = orcamento.pag6,
        pac = orcamento.pac
    )
    orc_bd.save()

def listar_orcamento(id):
    orcamentos = Orcamento.objects.filter(pac=id).all().order_by('-data')
    return orcamentos

def listar_orcamentos_id(id):
    orcamento = Orcamento.objects.get(id=id)
    return orcamento

def contar_orcamentos_id():
    contagem = Orcamento.objects.all().count()
    return contagem


def listar_orcamentos():
    return Orcamento.objects.all().order_by('-data')

def editar_orcamento(orcamento, orcamento_novo):
    orcamento.pac = orcamento_novo.pac
    orcamento.nomeorc = orcamento_novo.nomeorc
    orcamento.descr = orcamento_novo.descr
    orcamento.proc1 = orcamento_novo.proc1 
    orcamento.val1 = orcamento_novo.val1
    orcamento.pag1 = orcamento_novo.pag1
    orcamento.proc2 = orcamento_novo.proc2
    orcamento.val2 = orcamento_novo.val2
    orcamento.pag2 = orcamento_novo.pag2
    orcamento.proc3 = orcamento_novo.proc3
    orcamento.val3 = orcamento_novo.val3
    orcamento.pag3 = orcamento_novo.pag3
    orcamento.proc4 = orcamento_novo.proc4
    orcamento.val4 = orcamento_novo.val4
    orcamento.pag4 = orcamento_novo.pag4
    orcamento.proc5 = orcamento_novo.proc5
    orcamento.val5 = orcamento_novo.val5
    orcamento.pag5 = orcamento_novo.pag5
    orcamento.proc6 = orcamento_novo.proc6
    orcamento.val6 = orcamento_novo.val6
    orcamento.pag6 = orcamento_novo.pag6
    orcamento.save(force_update=True)

def remover_orcamento(orcamento):
    orcamento.delete()