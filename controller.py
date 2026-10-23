from decimal import Decimal, InvalidOperation

from model import Cliente, Conta


class BancoController:
    def __init__(self, banco, view):
        self.banco = banco
        self.view = view

        self.view.botao_criar.config(command=self.criar_conta)
        self.view.botao_consultar.config(command=self.consultar_conta)

    def criar_conta(self):
        nome, cpf, saldo_texto = self.view.ler_cadastro()

        if not nome or not cpf:
            self.view.exibir_erro("Preencha nome e CPF.")
            return

        try:
            saldo = Decimal(saldo_texto.replace(",", "."))

            if not saldo.is_finite() or saldo < 0:
                raise ValueError

            if saldo != saldo.quantize(Decimal("0.01")):
                raise ValueError

        except (InvalidOperation, ValueError):
            self.view.exibir_erro(
                "Informe um saldo não negativo com até duas casas decimais."
            )
            return

        cliente = Cliente(nome, cpf)

        conta = Conta(
            numero=self.banco.proximo_numero(),
            cliente=cliente,
            saldo=saldo,
        )

        self.banco.salvar(conta)
        self.view.exibir_conta(conta)

    def consultar_conta(self):
        try:
            numero = int(self.view.ler_numero())
        except ValueError:
            self.view.exibir_erro("Informe um número de conta válido.")
            return

        conta = self.banco.buscar(numero)

        if conta is None:
            self.view.exibir_erro("Conta não encontrada.")
            return

        self.view.exibir_conta(conta)