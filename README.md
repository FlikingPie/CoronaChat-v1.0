# 🤖 Corona Chatbot

Aplicación de escritorio desarrollada en Python que implementa un chatbot interactivo con interfaz gráfica moderna usando CustomTkinter.  
El bot es capaz de responder preguntas, aprender nuevas respuestas y utilizar síntesis de voz.

---

## 🚀 Características

- 💬 Interfaz gráfica amigable (CustomTkinter)
- 🧠 Sistema de respuestas basado en JSON
- 🔍 Búsqueda inteligente con coincidencias aproximadas (difflib)
- 🗣️ Respuestas por voz con pyttsx3
- 📚 Aprendizaje automático básico (guarda nuevas respuestas)
- 📜 Historial visual con scroll automático
- ⚡ Uso de threads para evitar bloqueos en la interfaz

---

## 📁 Estructura del proyecto
Corona-Chatbot/
│
├── main.py # Archivo principal
├── CoronaApp.py # Interfaz principal
├── chat.py # Lógica del chatbot
├── config.json # Base de conocimientos
└── README.md # Documentación


---

## ⚙️ Requisitos

Asegúrate de tener instalado Python 3.8 o superior.

Instala las dependencias con:

```bash
pip install customtkinter pyttsx3

## ▶️ Ejecución

Ejecuta el proyecto con:
python main.py


## 🧠 ¿Cómo funciona?
- Las claves representan palabras o frases clave
- Los valores son listas de posibles respuestas

## 📚 Aprendizaje automático básico
Si el bot no reconoce una entrada:
- Solicita al usuario una respuesta
- Guarda la nueva información en config.json
- Mejora con el tiempo

## 🗣️ Sistema de voz

El chatbot utiliza pyttsx3 para convertir texto a voz:
- No requiere internet
- Funciona en segundo plano usando threading

## 🔧 Posibles mejoras
-  🔗 Integración con APIs (clima, hora real, etc.)

-  🤖 Uso de modelos de IA (OpenAI, Hugging Face)

-  💾 Base de datos (SQLite)

-  🎤 Reconocimiento de voz

-  🌐 Versión web con Flask o Django

## Autor
 - Utrilla Solis Angel Kyle


