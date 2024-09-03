import tkinter as tk
from tkinter import scrolledtext

def run_script():
    script = text_area.get("1.0", tk.END)
    exec(script)

# Configura a janela principal
window = tk.Tk()
window.title("Editor de Código")

# Área de texto
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30)
text_area.pack(padx=10, pady=10)

# Botão para rodar o script
run_button = tk.Button(window, text="Rodar Script", command=run_script)
run_button.pack(pady=10)

window.mainloop()
