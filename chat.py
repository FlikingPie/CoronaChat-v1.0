import customtkinter
import random
import pyttsx3
import threading
import json
from tkinter import messagebox
from customtkinter import CTkInputDialog
from difflib import get_close_matches ## Detecta coincidencias

# Cargar datos
with open("config.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


def chat_w_bot():
    top = customtkinter.CTkToplevel()
    top.title("ChatBot Pro 🤖")
    top.geometry("420x550+450+200")
    top.resizable(False, False)

    # ===== CONTENEDOR CON SCROLL =====
    frame_principal = customtkinter.CTkFrame(top)
    frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = customtkinter.CTkCanvas(frame_principal)
    scrollbar = customtkinter.CTkScrollbar(frame_principal, command=canvas.yview)

    frame_chat = customtkinter.CTkFrame(canvas)

    frame_chat.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_chat, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ===== INPUT =====
    entrada_mensaje = customtkinter.CTkEntry(top, width=300)
    entrada_mensaje.pack(pady=10)

    # ===== FUNCION VOZ =====
    def hablar(texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        engine.stop()

    # ===== ENVIAR MENSAJE =====
    def enviar_mensaje(event=None):
        entrada = entrada_mensaje.get().lower().strip()

        if not entrada:
            messagebox.showwarning("Advertencia", "Escriba un mensaje")
            return

        # Usuario
        usuario = customtkinter.CTkLabel(
            frame_chat,
            text=entrada,
            fg_color="#DCF8C6",
            corner_radius=10,
            padx=10,
            pady=5,
            wraplength=250
        )
        usuario.pack(anchor="e", pady=3)

        encontrado = False

        # ===== IA MÁS INTELIGENTE =====
        claves = list(datos.keys())
        coincidencias = get_close_matches(entrada, claves, n=1, cutoff=0.6)

        if coincidencias:
            clave = coincidencias[0]
            respuesta = random.choice(datos[clave])
            encontrado = True

        # ===== SI NO ENTIENDE =====
        if not encontrado:
            respuesta = "No entiendo 😢"

            dialogo = CTkInputDialog(
                text="¿Qué debería responder? (separa con coma)",
                title="Aprender"
            )
            nueva_respuesta = dialogo.get_input()

            if nueva_respuesta:
                lista_respuestas = [r.strip() for r in nueva_respuesta.split(",")]

                if entrada in datos:
                    datos[entrada].extend(lista_respuestas)
                else:
                    datos[entrada] = lista_respuestas

                with open("config.json", "w", encoding="utf-8") as file:
                    json.dump(datos, file, indent=4, ensure_ascii=False)

                messagebox.showinfo("Info", "Aprendido correctamente ✅")

        # IA
        ia = customtkinter.CTkLabel(
            frame_chat,
            text=respuesta,
            fg_color="#EAEAEA",
            corner_radius=10,
            padx=10,
            pady=5,
            wraplength=250
        )
        ia.pack(anchor="w", pady=3)

        # ===== SCROLL AUTOMÁTICO =====
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)

        # ===== VOZ EN THREAD =====
        threading.Thread(target=hablar, args=(respuesta,), daemon=True).start()

        entrada_mensaje.delete(0, customtkinter.END)

    # Enter para enviar
    entrada_mensaje.bind("<Return>", enviar_mensaje)