import tkinter as tk
from tkinter import messagebox


class BancoView:
    def __init__(self, janela):
        self.janela = janela
        janela.title("Banco — Arquitetura MVC")
        janela.geometry("480x520")

        tk.Label(
            janela,
            text="Cadastro de conta",
            font=("Arial", 16),
        ).pack(pady=10)

        tk.Label(janela, text="Nome").pack()
        self.nome = tk.Entry(janela, width=40)
        self.nome.pack(pady=4)

        tk.Label(janela, text="CPF").pack()
        self.cpf = tk.Entry(janela, width=40)
        self.cpf.pack(pady=4)

        tk.Label(janela, text="Saldo inicial").pack()
        self.saldo = tk.Entry(janela, width=40)
        self.saldo.pack(pady=4)

        self.botao_criar = tk.Button(janela, text="Criar conta")
        self.botao_criar.pack(pady=10)

        tk.Label(janela, text="Número da conta para consultar").pack()
        self.numero = tk.Entry(janela, width=40)
        self.numero.pack(pady=4)

        self.botao_consultar = tk.Button(
            janela,
            text="Exibir dados da conta",
        )
        self.botao_consultar.pack(pady=10)

        self.resultado = tk.Label(
            janela,
            text="",
            justify="left",
            font=("Arial", 12),
            wraplength=440,
        )
        self.resultado.pack(pady=10)

    def ler_cadastro(self):
        return (
            self.nome.get().strip(),
            self.cpf.get().strip(),
            self.saldo.get().strip(),
        )

    def ler_numero(self):
        return self.numero.get().strip()

    def exibir_conta(self, conta):
        saldo = f"{conta.saldo:.2f}".replace(".", ",")

        self.resultado.config(
            text=(
                f"Conta: {conta.numero}\n"
                f"Nome: {conta.cliente.nome}\n"
                f"CPF: {conta.cliente.cpf}\n"
                f"Saldo: R$ {saldo}"
            )
        )

        self.numero.delete(0, tk.END)
        self.numero.insert(0, str(conta.numero))

    def exibir_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)