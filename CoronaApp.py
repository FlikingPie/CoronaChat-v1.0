import customtkinter
from chat import chat_w_bot

class CoronaApp:
    def conversar(self):
        chat_w_bot()

    def configurar(self):
        pass

    def __init__(self, root):
        self.root = root
        self.root.title("Corona Chatbot")
        self.root.geometry("400x300+450+250")
        self.root.resizable(False, False)

        self.boton1 = customtkinter.CTkButton(root, text="Conversar", width=100, command=self.conversar)
        self.boton1.pack(pady=5)

        self.boton2 = customtkinter.CTkButton(root, text="Configurar", width=100, command=self.configurar)
        self.boton2.pack(pady=5)