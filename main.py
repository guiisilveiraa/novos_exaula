import tkinter as tk

from controller import BancoController
from model import BancoDados
from view import BancoView


def main():
    janela = tk.Tk()
    banco = BancoDados()
    view = BancoView(janela)
    controller = BancoController(banco, view)

    janela.mainloop()


if __name__ == "__main__":
    main()