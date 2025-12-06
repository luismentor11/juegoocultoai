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

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]  # viene de los secrets de Streamlit Cloud


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

    if "chat" not in st.session_state:
        st.session_state.chat = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    user_input = st.text_area("Escribí acá lo que te pasa:", height=150)

    if st.button("Jugar / Ver diagnóstico"):
        if user_input.strip():
            st.session_state.chat.append({"role": "user", "content": user_input.strip()})
            with st.spinner("Pensando..."):
                respuesta = call_openai(st.session_state.chat)
            st.session_state.chat.append({"role": "assistant", "content": respuesta})

    mensajes_ai = [m for m in st.session_state.chat if m["role"] == "assistant"]
    if mensajes_ai:
        st.markdown("### Respuesta del Juego Oculto (OpenAI):")
        st.write(mensajes_ai[-1]["content"])


if __name__ == "__main__":
    main()
