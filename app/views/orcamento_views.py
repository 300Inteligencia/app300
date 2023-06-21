from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import render_to_string
from django.core.mail import send_mail

from orcamentos import settings

from ..forms.orcamento_forms import OrcamentoForm
from ..entidades import orcamento
from ..services import orcamento_services, cliente_service
from ..views import cliente_views
from ..models import Cliente, Orcamento

@user_passes_test(lambda u: u.cargo==1)
def inserir_orcamento(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    cliente = cliente.id
    if request.method == "POST":
        form_orcamento = OrcamentoForm(request.POST)
        pac = cliente_service.listar_cliente_id(id)
        if form_orcamento.is_valid():
            nomeorc = form_orcamento.cleaned_data["nomeorc"]
            descr = form_orcamento.cleaned_data["descr"]
            proc1 = form_orcamento.cleaned_data["proc1"]
            val1 = form_orcamento.cleaned_data["val1"]
            pag1 = form_orcamento.cleaned_data["pag1"]
            proc2 = form_orcamento.cleaned_data["proc2"]
            val2 = form_orcamento.cleaned_data["val2"]
            pag2 = form_orcamento.cleaned_data["pag2"]
            proc3 = form_orcamento.cleaned_data["proc3"]
            val3 = form_orcamento.cleaned_data["val3"]
            pag3 = form_orcamento.cleaned_data["pag3"]
            proc4 = form_orcamento.cleaned_data["proc4"]
            val4 = form_orcamento.cleaned_data["val4"]
            pag4 = form_orcamento.cleaned_data["pag4"]
            proc5 = form_orcamento.cleaned_data["proc5"]
            val5 = form_orcamento.cleaned_data["val5"]
            pag5 = form_orcamento.cleaned_data["pag5"]
            proc6 = form_orcamento.cleaned_data["proc6"]
            val6 = form_orcamento.cleaned_data["val6"]
            pag6 = form_orcamento.cleaned_data["pag6"]
            orcamento_novo = orcamento.Orcamentos(pac=pac, nomeorc=nomeorc,descr=descr, proc1=proc1, val1=val1, pag1=pag1, proc2=proc2,val2=val2, pag2=pag2, proc3=proc3, val3=val3, pag3=pag3, proc4=proc4, val4=val4, pag4=pag4, proc5=proc5, val5=val5, pag5=pag5, proc6=proc6, val6=val6, pag6=pag6)
            orcamento_services.cadastrar_orcamento(orcamento_novo)
            url = reverse(cliente_views.listar_cliente_id, args=[cliente])
            return redirect(url)
    else:
        form_orcamento = OrcamentoForm()
    return render(request, 'orcamentos/form_orcamento.html', {'form_orcamento': form_orcamento})

@user_passes_test(lambda u: u.cargo==1)
def listar_orcamentos(request):
    orcamentos = orcamento_services.listar_orcamento()
    return render(request, 'orcamentos/lista_orcamentos.html', {'orcamentos': orcamentos})

@user_passes_test(lambda u: u.cargo==1)
def listar_orcamento_id(request, id):
    orcamento = orcamento_services.listar_orcamentos_id(id)
    cliente = cliente_service.listar_cliente_id(orcamento.pac.id)
    return render(request, 'orcamentos/lista_orcamentos.html', {'orcamento': orcamento, 'cliente':cliente})

@user_passes_test(lambda u: u.cargo==1)
def enviar_email_orcamento(request, id):
    orcamento = orcamento_services.listar_orcamentos_id(id)
    cliente = cliente_service.listar_cliente_id(orcamento.pac.id)
    assunto = "Orçamento"
    html_conteudo = render_to_string('orcamentos/orcamento_email.html', {'orcamento':orcamento})
    corpo_email = "Resumo do Orçamento"
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [cliente.email,]
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_conteudo)
    return redirect('listar_orcamento_id', id)

@user_passes_test(lambda u: u.cargo==1)
def remover_orcamento(request, id):
    orcamento = orcamento_services.listar_orcamentos_id(id)
    cliente = orcamento.pac.id
    if request.method == "POST":
        orcamento_services.remover_orcamento(orcamento)
        cliente_id = cliente
        url = reverse(cliente_views.listar_cliente_id, args=[cliente_id])
        return redirect(url)
    return render(request, 'orcamentos/confirma_exclusao_orcamento.html', {'orcamento': orcamento})

@user_passes_test(lambda u: u.cargo==1)
def editar_orcamento(request, id):
    orcamento_editar = orcamento_services.listar_orcamentos_id(id)
    cliente = cliente_service.listar_cliente_id(orcamento_editar.pac.id)
    form_orcamento = OrcamentoForm(request.POST or None, instance=orcamento_editar)
    if form_orcamento.is_valid():
        pac = form_orcamento.cleaned_data["pac"]
        nomeorc = form_orcamento.cleaned_data["nomeorc"]
        descr = form_orcamento.cleaned_data["descr"]
        proc1 = form_orcamento.cleaned_data["proc1"]
        val1 = form_orcamento.cleaned_data["val1"]
        pag1 = form_orcamento.cleaned_data["pag1"]
        proc2 = form_orcamento.cleaned_data["proc2"]
        val2 = form_orcamento.cleaned_data["val2"]
        pag2 = form_orcamento.cleaned_data["pag2"]
        proc3 = form_orcamento.cleaned_data["proc3"]
        val3 = form_orcamento.cleaned_data["val3"]
        pag3 = form_orcamento.cleaned_data["pag3"]
        proc4 = form_orcamento.cleaned_data["proc4"]
        val4 = form_orcamento.cleaned_data["val4"]
        pag4 = form_orcamento.cleaned_data["pag4"]
        proc5 = form_orcamento.cleaned_data["proc5"]
        val5 = form_orcamento.cleaned_data["val5"]
        pag5 = form_orcamento.cleaned_data["pag5"]
        proc6 = form_orcamento.cleaned_data["proc6"]
        val6 = form_orcamento.cleaned_data["val6"]
        pag6 = form_orcamento.cleaned_data["pag6"]
        orcamento_novo = orcamento.Orcamentos(pac=pac, nomeorc=nomeorc, descr=descr, proc1=proc1, val1=val1, pag1=pag1, proc2=proc2, val2=val2, pag2=pag2, proc3=proc3, val3=val3, pag3=pag3, proc4=proc4, val4=val4, pag4=pag4, proc5=proc5, val5=val5, pag5=pag5, proc6=proc6, val6=val6, pag6=pag6)
        orcamento_services.editar_orcamento(orcamento_editar, orcamento_novo)
        return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})
    return render(request, 'orcamentos/form_orcamento.html', {'form_orcamento': form_orcamento})

@user_passes_test(lambda u: u.cargo==1)
def contagem_orcamentos(request):
    contagem = orcamento_services.contar_orcamentos_id()
    return render(request, 'orcamentos/contagem_orcamentos.html', {'contagem': contagem})
