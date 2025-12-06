import streamlit as st
import requests

# ---------- CONFIG ----------

SYSTEM_PROMPT = """
Sos EL JUEGO OCULTO, un agente ontológico que ayuda a la persona
a ver el juego psicológico que viene jugando sin darse cuenta
y a empezar a diseñar un juego nuevo más consciente.

Estilo:
- Directo, honesto, sin chamuyo pero con respeto.
- Hacés preguntas poderosas, no sermones.
- Usás "vos", no "tú".
- No sos terapeuta ni médico.

Objetivo en esta VERSIÓN SIMPLE:
1. Escuchar el problema central que la persona trae.
2. Devolverle qué "juego viejo" parece estar jugando.
3. Hacer 1 o 2 preguntas potentes para que vea ese juego.
4. Sugerir un posible "juego nuevo" en pocas líneas.

Reglas:
- Respuestas cortas (5 a 10 líneas máximo).
- Una sola intervención por vez.
"""

# La API key viene de los secrets de Streamlit Cloud
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


def call_openai(messages):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-4.1-mini",  # modelo barato y fuerte en razonamiento
        "messages": messages,
        "temperature": 0.7,
    }

    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    j = resp.json()
    return j["choices"][0]["message"]["content"]


def main():
    st.title("El Juego Oculto – Test con OpenAI")
    st.write("Contame en qué área de tu vida sentís más ruido o conflicto hoy, y qué es lo que más te duele de eso.")

    # Inicializar historial de chat
    if "chat" not in st.session_state:
        st.session_state.chat = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    # Mostrar historial como burbujas
    for msg in st.session_state.chat:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(msg["content"])

    # Input de chat abajo
    prompt = st.chat_input("Escribí acá lo que te pasa:")
    if prompt:
        # Mensaje del usuario
        st.session_state.chat.append({"role": "user", "content": prompt})

        # Respuesta del Juego Oculto (OpenAI)
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                respuesta = call_openai(st.session_state.chat)
            st.session_state.chat.append({"role": "assistant", "content": respuesta})
            st.write(respuesta)


if __name__ == "__main__":
    main()
