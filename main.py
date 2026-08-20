from google import genai 
import tkinter as tk

janela = tk.Tk()
janela.title("primeira ia ")
janela.geometry("400x300")
API_key = "minha_minha_chave"
cliente = genai.Client(api_key = API_key)


def enviar_pergunta():
    pergunta = albiente.get()
    if pergunta == "":
        resposta.delete("1.0", tk.END)
        resposta.insert(tk.END, "por favor, digite uma pergunta.")
    else:
        resposta.delete("1.0", tk.END)
        resposta.insert(tk.END, "processando. . .")
        janela.update()
    try:
        resposta_ia = cliente.models.generate_content(
            model = "gemini-3.6-flash",
             contents = pergunta
        )
        resposta.delete("1.0", tk.END)
        resposta.insert(tk.END, resposta_ia.text)
    except ValueError :
        resposta.delete("1.0", tk.END)
        print("Erro ao gerar resposta:")

resposta = tk.Text(janela, wrap=tk.WORD)
rolagem = tk.Scrollbar(janela)
rolagem.config(command=resposta.yview)
rolagem.pack(side=tk.RIGHT, fill=tk.Y)
resposta.config(yscrollcommand=rolagem.set)


albiente = tk.Entry(janela)

botao = tk.Button(janela, text="Enviar", command=enviar_pergunta)


albiente.pack()
botao.pack()
resposta.pack()

janela.mainloop()