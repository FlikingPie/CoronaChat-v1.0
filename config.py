from datetime import datetime
hora = datetime.now().strftime("%H:%M:%S")

preguntas_respuestas={
    "hola":["Hola!!", "¿Hola, Como va tu día?", "Muy buenas, te gustaría conversar un momento"],
    "hora":[f'Hora actual: {hora}', f'{hora}'],
    "nombre" : ["Soy tu chatbot 🤖", "Aún no tengo nombre 😅"],
    "como estas": ["Estoy bien 😄 ¿y tú?", "Todo genial por aquí"]
}
