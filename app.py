import tkinter as tk

def carregar_arquivo():
    try:
        with open('dados.txt', 'r') as file:
            for line in file:
                if line.count('|') == 3:
                    listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

def adicionar_dados():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    idade = entry_idade.get()

    if nome and cpf and endereco and idade:
        listbox.insert(tk.END, f"{nome} | {cpf} | {endereco} | {idade}")

        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
    else:
        print("Preencha todos os campos.")  

def salvar_dados():
    with open('dados.txt', 'w') as file:
        for i in range(listbox.size()):
            file.write(listbox.get(i) + '\n')
    print("Dados salvos com sucesso.")

def deletar_dados():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        salvar_dados() 
    except IndexError:
        print("Selecione um item para deletar.")  

def carregar_dados(event):
    try:
        selected_item = listbox.get(listbox.curselection())
        if selected_item.count('|') == 3:
            nome, cpf, endereco, idade = selected_item.split(" | ")
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome)
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, cpf)
            entry_endereco.delete(0, tk.END)
            entry_endereco.insert(0, endereco)
            entry_idade.delete(0, tk.END)
            entry_idade.insert(0, idade)
    except IndexError:
        pass

def atualizar_dados():
    try:
        selected_index = listbox.curselection()[0]  
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        endereco = entry_endereco.get()
        idade = entry_idade.get()

        if nome and cpf and endereco and idade:
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"{nome} | {cpf} | {endereco} | {idade}")
        else:
            print("Preencha todos os campos para atualizar.")
    except IndexError:
        print("Selecione um item para atualizar.")

window = tk.Tk()
window.title("Agenda")

entry_nome = tk.Entry(window, width=30)
entry_cpf = tk.Entry(window, width=30)
entry_endereco = tk.Entry(window, width=30)
entry_idade = tk.Entry(window, width=30)

btn_adicionar = tk.Button(window, text="Adicionar", command=adicionar_dados)
btn_atualizar = tk.Button(window, text="Atualizar", command=atualizar_dados)
btn_salvar = tk.Button(window, text="Salvar", command=salvar_dados)
btn_deletar = tk.Button(window, text="Deletar", command=deletar_dados)

listbox = tk.Listbox(window, width=50, height=10)
listbox.bind("<<ListboxSelect>>", carregar_dados)

entry_nome.grid(row=0, column=1)
entry_cpf.grid(row=1, column=1)
entry_endereco.grid(row=2, column=1)
entry_idade.grid(row=3, column=1)
btn_adicionar.grid(row=4, column=0)
btn_atualizar.grid(row=4, column=1)
btn_salvar.grid(row=4, column=2)
btn_deletar.grid(row=4, column=3)
listbox.grid(row=5, column=0, columnspan=4)

tk.Label(window, text="Nome:").grid(row=0, column=0)
tk.Label(window, text="CPF:").grid(row=1, column=0)
tk.Label(window, text="Endereço:").grid(row=2, column=0)
tk.Label(window, text="Idade:").grid(row=3, column=0)

carregar_arquivo()

window.mainloop()


