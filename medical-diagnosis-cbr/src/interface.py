import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Para melhorar a organização da tabela
from diagnosis import carregar_base_de_dados, recuperar_diagnostico

def start_interface():
    """Inicia a interface gráfica do usuário."""
    # Carregar a base de dados
    base_de_dados = carregar_base_de_dados('data/base_de_casos.csv')

    # Função para processar a entrada do usuário
    def processar_input():
        sintomas_input = entry_sintomas.get()
        resultado = recuperar_diagnostico(sintomas_input, base_de_dados)

        # Verifica se o resultado é uma string (não é uma tabela)
        if isinstance(resultado, str):
            messagebox.showinfo("Resultados", resultado)
        else:
            mostrar_resultados(resultado)

    # Função para exibir os resultados em uma tabela
    def mostrar_resultados(resultado):
        # Limpar a tabela antes de inserir novos dados
        for row in tree.get_children():
            tree.delete(row)

        # Inserir os resultados na tabela
        for index, row in resultado.iterrows():
            tree.insert("", "end", values=(row['Sintomas'], row['Doença Diagnostica'], row['Tratamento']))

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Sistema de Diagnóstico Médico")
    root.geometry("600x400")  # Define o tamanho inicial da janela

    # Label e entrada para os sintomas
    label = tk.Label(root, text="Insira os sintomas (separados por vírgula):")
    label.pack(pady=10)

    entry_sintomas = tk.Entry(root, width=70)
    entry_sintomas.pack(pady=10)

    button = tk.Button(root, text="Diagnosticar", command=processar_input)
    button.pack(pady=10)

    # Tabela para exibir os resultados
    cols = ("Sintomas", "Doença Diagnostica", "Tratamento")
    tree = ttk.Treeview(root, columns=cols, show="headings")
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=150)  # Define a largura das colunas
    
    tree.pack(pady=20, fill="both", expand=True)  # Expande a tabela para preencher a janela

    # Barra de rolagem horizontal
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Iniciar a interface
    root.mainloop()
