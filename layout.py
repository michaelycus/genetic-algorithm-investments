from tkinter import ttk as tk_table

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import constants
from genetic import simulate

SUITABILITY = ["Conservador", "Moderado", "Arrojado", "Agressivo"]


# Função para criar tabelas dinâmicas
def create_table(main_frame, data, columns):
    table = tk_table.Treeview(main_frame, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor=CENTER)

    for item in data:
        table.insert("", END, values=list(item.values()))

    table.pack(expand=True, fill=BOTH)


# Função para alternar entre as seções
def change_section(section, app, main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()

    if section == "Home":

        home = ttk.Frame(app, padding=5)
        home.pack(side=RIGHT, expand=True, fill=BOTH)

        labelInvest = ttk.Label(home, text="Investimento: ")
        labelInvest.grid(row=0, column=0)

        # Criando a validação
        vcmd = (app.register(validate_currency_entry), "%P")

        entryInvest = ttk.Entry(home, validate="key", validatecommand=vcmd)
        entryInvest.insert(0, 10000)
        entryInvest.grid(row=0, column=1, padx=5, pady=5)

        labelSuitability = ttk.Label(home, text="Suitability: ")
        labelSuitability.grid(row=1, column=0, padx=5, pady=5)

        comboSuitability = ttk.Combobox(home)
        comboSuitability["values"] = SUITABILITY
        comboSuitability.current(0)
        comboSuitability.grid(row=1, column=1, padx=5, pady=5)

        buttonSimulate = ttk.Button(
            home, text="Simular", command=lambda: simulate(float(entryInvest.get()))
        )
        buttonSimulate.grid(row=3, column=0, padx=5, pady=5)

        labelStock = ttk.Label(home, text="Ações")
        labelStock.grid(row=4, column=0, padx=5, pady=5)

        labelMaxStock = ttk.Label(home, text="Máximo:")
        labelMaxStock.grid(row=4, column=1, padx=5, pady=5)

        max_stocks = 1
        maxScale = ttk.Scale(home, from_=0, to=10, variable=max_stocks)
        maxScale.grid(row=4, column=2, padx=5, pady=5)

        labelVarMaxStock = ttk.Label(home, text=max_stocks)
        labelVarMaxStock.grid(row=4, column=3, padx=5, pady=5)

    elif section == "Ações":
        create_table(
            main_frame,
            constants.STOCKS,
            [
                "Tipo",
                "Código",
                "Nome",
                "Preço",
                "Setor",
                "Volatidade",
                "DY",
                "P/VPA",
                "Valorização %",
            ],
        )
    elif section == "Fiis":
        create_table(
            main_frame,
            constants.FIIS,
            [
                "Tipo",
                "Código",
                "Nome",
                "Preço",
                "Setor",
                "Volatidade",
                "DY",
                "P/VPA",
                "Valorização %",
            ],
        )


def validate_currency_entry(text):
    # Verifica se o valor é vazio (permite deletar todo o conteúdo)
    if text == "":
        return True

    # Permite apenas números e uma única vírgula
    try:
        # Substitui a vírgula por um ponto para validação de float
        float(text.replace(",", "."))
        # Verifica se o valor tem no máximo uma vírgula
        if text.count(",") <= 1:
            # Verifica se há no máximo duas casas decimais
            if len(text.split(",")[1]) <= 2 if "," in text else True:
                return True
        return False
    except ValueError:
        return False


def init_layout():
    # Criando a janela principal
    app = ttk.Window("App de Investimentos", themename="flatly", size=(800, 600))

    # Criando os frames

    side_menu = ttk.Frame(app, padding=10)
    side_menu.pack(side=LEFT, fill=Y)

    main_frame = ttk.Frame(app, padding=10)
    main_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    # Criando botões do menu lateral
    ttk.Button(
        side_menu, text="Home", command=lambda: change_section("Home", app, main_frame)
    ).pack(pady=5)
    ttk.Button(
        side_menu,
        text="Ações",
        command=lambda: change_section("Ações", app, main_frame),
    ).pack(pady=5)
    ttk.Button(
        side_menu,
        text="Fiis",
        command=lambda: change_section("Fiis", app, main_frame),
    ).pack(pady=5)

    # Inicializando com a tela "Home"
    change_section("Home", app, main_frame)

    app.mainloop()
