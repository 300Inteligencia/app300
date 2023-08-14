from django.contrib.auth.models import AbstractUser
from django.db import models
from django_localflavor_br.br_states import STATE_CHOICES

# Create your models here.

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, null=False, blank=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    telefone = models.CharField(max_length=11,null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)
    medico_choices = [
        (1, 'Cristiano Dias da Silveira Ramos'),
        (2, 'Érika Lawall Lopoes Ramos')
    ]
    medico = models.IntegerField(choices=medico_choices, null=False, blank=False)

class Orcamento(models.Model):
    forma_pagamento_choices = [
        (1, '1x Cartão de Crédito'),
        (2, '2x Cartão de Crédito'),
        (3, '3x Cartão de Crédito'),
        (4, '4x Cartão de Crédito'),
        (5, '5x Cartão de Crédito'),
        (6, '6x Cartão de Crédito'),
        (7, 'Dinheiro')
    ]

    cirurgias_choices = [
        (1, 'Abdominoplastia'),
        (2, 'Mini-abdominoplastia'),
        (3, 'Blefaroplastia Superior'),
        (4, 'Blefaroplastia Inferior'),
        (5, 'Blefaroplastia Superior e Inferior'),
        (6, 'Braquioplastia'),
        (7, 'Face'),
        (8, 'Lipoaspiração'),
        (9, 'Lipoaspiração de Dorso'),
        (10, 'Lipoaspiração de Submento'),
        (11, 'Mama Redutora'),
        (12, 'Mamoplastia de Aumento'),
        (13, 'Mastopexia'),
        (14, 'Mastopexia com Prótese'),
        (15, 'Ninfoplastia'),
        (16, 'Otoplastia'),
        (17, 'Retoque'),
        (18, 'Rinoplastia'),
        (19, 'Tumores cutâneos')
    ]   

    pac = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    
    nomeorc = models.CharField(max_length=200, null=False, blank=False)
    descr = models.CharField(max_length=400, null=False, blank=False)

    proc1 = models.IntegerField(choices=cirurgias_choices, null=False, blank=False)
    val1 = models.FloatField(null=True, blank=True)
    pag1 = models.IntegerField(choices=forma_pagamento_choices, null=False, blank=False)

    proc2 = models.IntegerField(choices=cirurgias_choices, null=True, blank=True)
    val2 = models.FloatField(null=True, blank=True)
    pag2 = models.IntegerField(choices=forma_pagamento_choices, null=True, blank=True)

    proc3 = models.IntegerField(choices=cirurgias_choices, null=True, blank=True)
    val3 = models.FloatField(null=True, blank=True)
    pag3 = models.IntegerField(choices=forma_pagamento_choices, null=True, blank=True)

    proc4 = models.IntegerField(choices=cirurgias_choices, null=True, blank=True)
    val4 = models.FloatField(null=True, blank=True)
    pag4 = models.IntegerField(choices=forma_pagamento_choices, null=True, blank=True)

    proc5 = models.IntegerField(choices=cirurgias_choices, null=True, blank=True)
    val5 = models.FloatField(null=True, blank=True)
    pag5 = models.IntegerField(choices=forma_pagamento_choices, null=True, blank=True)

    proc6 = models.IntegerField(choices=cirurgias_choices, null=True, blank=True)
    val6 = models.FloatField(null=True, blank=True)
    pag6 = models.IntegerField(choices=forma_pagamento_choices, null=True, blank=True)

    def total(self):
        return (self.val1 or 0) + (self.val2 or 0) + (self.val3 or 0) + (self.val4 or 0) + (self.val5 or 0) + (self.val6 or 0)

class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Médico'),
        (2, 'Suporte'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)
