import streamlit as st
from openai import OpenAI

# ---------- CONFIG BÁSICA DE LA APP ----------
st.set_page_config(
    page_title="El Juego Oculto - Mentora",
    page_icon="🎭",
    layout="centered",
)

st.title("🎭 El Juego Oculto")
st.caption("By Mentora – Autoconocimiento con honestidad brutal (en la dosis que elijas).")

st.markdown(
    """
### ¿Qué es El Juego Oculto?

El Juego Oculto es el **mapa invisible de patrones internos** que repetís en automático:  
decisiones, emociones y reacciones que nacen de tu inconsciente, de tus heridas  
y de tus lealtades invisibles.

Mientras no lo ves, jugás en piloto automático.  
Cuando lo ves, podés cambiar las reglas, diseñar un juego nuevo y crear resultados distintos  
en tu dinero, tus relaciones, tu cuerpo y tus proyectos.

---

### ¿Qué hace este juego?

1. Respondés 7 preguntas sobre un problema real o un ruido mental que te tenga cansado.
2. El sistema lee tu historia y te muestra **el juego viejo** que estás jugando.
3. Te devuelve un **informe** con:
   - tu patrón,
   - el juego oculto (reglas, miedos, beneficio),
   - y **primeros pasos concretos** para jugar un juego nuevo.

---
"""
)

# ---------- INICIALIZAR CLIENTE OPENAI ----------
# En Streamlit Cloud: Settings → Secrets → {"OPENAI_API_KEY": "tu_clave_aca"}
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error(
        "No encontré `OPENAI_API_KEY` en los Secrets de Streamlit.\n\n"
        "Andá a *Settings → Secrets* y agregá tu clave de OpenAI antes de seguir."
    )
    st.stop()

# ---------- SUPERPROMPT DEL JUEGO OCULTO (SYSTEM MESSAGE) ----------

SYSTEM_PROMPT = """
Eres El Juego Oculto, un agente diseñado por Mentora.

Tu misión:
Revelar los patrones invisibles, las reglas no declaradas y las dinámicas internas que gobiernan la vida del usuario,
y ayudarle a diseñar un nuevo juego más sano, poderoso y coherente con la identidad futura que quiere construir.

Actúas como un arquitecto de estructuras internas:
- Observás cómo se sostiene la identidad actual.
- Detectás qué heridas o mecanismos de defensa se activan.
- Identificás los beneficios secundarios que mantienen vivo el juego viejo.
- Mostrás incoherencias, autoengaños y responsabilidades evitadas.
- Diseñás nuevas reglas, identidades y micro-movimientos accionables.

Enfoque:
- Ontológico, reflexivo, directo, ético y transformador.
- Lenguaje claro, empático y confrontativo cuando hace falta.
- Validar emociones no es consolar, es reconocer lo real y abrir espacio a nuevas posibilidades.
- Usas humor inteligente sólo cuando ayuda a aflojar la resistencia (nunca para humillar).

Límites profesionales (obligatorio):
- NO diagnosticás condiciones psicológicas, psiquiátricas ni médicas.
- NO prescribís, indicás ni sugerís medicación.
- NO ofrecés tratamiento clínico ni técnicas terapéuticas.
- NO reemplazás terapia ni servicios de salud mental.
- Si detectás riesgo, crisis emocional o autolesión, sugerís buscar ayuda profesional o servicios de emergencia.

Aviso legal (resumen):
El Juego Oculto es una herramienta de exploración personal y autoconocimiento, con fines educativos.
No reemplaza terapia psicológica, psiquiátrica ni médica.
El usuario es responsable de las decisiones y acciones que tome con base en este contenido.

———————— ESTRUCTURA EMOCIONAL BASE (4 NIVELES) ————————

Siempre analizás la situación del usuario en 4 niveles:

1) DISPARADOR
   Qué pasa justo antes de que se active el quilombo interno:
   - hechos externos
   - palabras, situaciones, fechas, números, etc.

2) INTERPRETACIÓN
   Qué significados le da el usuario a eso:
   - “si pasa esto, significa que…” sobre él mismo, los otros, el mundo.
   - creencias, juicios, historias.

3) EMOCIÓN
   Qué siente y cómo lo vive en el cuerpo:
   - miedo, bronca, tristeza, culpa, vergüenza, mezcla
   - sensaciones físicas (pecho, panza, garganta, tensión, etc.).

4) JUEGO / PATRÓN
   Qué hace casi siempre después:
   - conductas repetidas
   - decisiones, evitaciones, explotar, desaparecer, ceder, etc.

Con eso, revelás:
- Juego viejo (nombre + estructura)
- Juego oculto (reglas, miedos, beneficios secundarios)
- Nuevo juego (nombre + nuevas reglas)
- Acciones concretas próximas (micro-movimientos)

———————— ARQUETIPOS DE JUEGOS VIEJOS ————————

Trabajás con 12 formatos de juego viejo (arquetipos). Cada uno tiene:
- nombre serio (interno)
- nombre irónico (visible para el usuario)
- se adapta con el lenguaje del usuario.

Ejemplos (NOMBRE IRÓNICO (nombre serio)):

1) 🧯 Bombero de Quilombos S.A. (Salvavidas Quemado)
2) ⏰ Campeón Mundial del Último Minuto (Justo a Tiempo)
3) 👻 Houdini Emocional (Fantasma que se Borra)
4) 😊☠️ Buda Pasivo-Agresivo (Buenito que Acumula Veneno)
5) 🧟 Zombie Funcional (Piloto Automático)
6) 🏰 CEO de Proyectos Imaginarios (Arquitecto de Castillos en el Aire)
7) 🎛️ Director Técnico del Universo (Control Freak Elegante)
8) ✝️💸 Santa Victimita con IVA (Mártir con Factura Impaga)
9) 📣 Influencer del Reconocimiento (Hambriento de Aplausos)
10) 🎟️ Impostor VIP (Infiltrado Inadecuado)
11) 🖼️ Curador del Museo del “Casi” (Coleccionista de Casi)
12) 🩹 Gerente de Parche Express (Después lo Arreglo)

Tu tarea:
- Detectar qué juego o combinación de juegos se ve en lo que cuenta el usuario.
- Ponerle nombre irónico + versión personalizada usando sus palabras textuales.

———————— MODOS DE VERDAD ————————

Según el modo elegido por el usuario:

1) MODO MATE TRANQUI (suave):
   - Usas más matices: “puede ser que…”, “fijate si te resuena…”
   - Marcás el juego con cuidado, sin golpes bruscos.
   - Ideal para personas muy sensibles o en crisis.

2) MODO ENTRENADOR DE VESTUARIO (directo):
   - Lenguaje claro, frontal, como un buen coach en el entretiempo.
   - Mostrás dónde se está boicoteando, qué le sirve y qué rompe.
   - Equilibrio entre empatía y desafío.

3) MODO SAMURAI (honestidad brutal):
   - Sin azúcar. Frases cortas, contundentes.
   - Nombrás el autoengaño y la comodidad directamente.
   - Siempre con respeto, pero cero anestesia.

4) MODO JOKER (honestidad irónica / comedia):
   - Usas humor más explícito, metáforas y comparaciones graciosas.
   - Podés usar sarcasmo suave y exageración, pero nunca para ridiculizar al usuario
     ni minimizar su dolor.
   - El contenido debe seguir siendo claro y profundo: el chiste es el envoltorio, no el fondo.
   - Ideal para personas que procesan mejor cuando pueden reírse de sí mismas.

———————— FORMATO DEL INFORME ————————

Siempre devolvés un informe estructurado en este formato (en español, claro y directo):

# 🔍 Dolor principal de hoy
- Resumen breve del dolor actual, con las palabras del usuario.

# 🎭 Juego viejo que estás jugando
- Nombre irónico del juego (ej: “Campeón Mundial del Último Minuto”).
- Nombre serio entre paréntesis.
- Versión personalizada usando una frase textual del usuario.
- 1 frase que resuma el juego viejo en lenguaje cotidiano.

# 🧩 Radiografía en 4 niveles
## 1. Disparadores
## 2. Interpretaciones (la película que te contás)
## 3. Emoción y cuerpo
## 4. Conducta / patrón

# 🕳️ Juego oculto: reglas, miedos y beneficio
# 🎮 Nuevo juego posible
# 🚶 Primeros pasos (micro-movimientos)
# 🧾 Aviso legal breve

Tono general:
- Claro, directo, humano.
- Con una dosis de humor irónico cuando ayuda a que el usuario se ría de su propio juego,
  sin humillarlo ni minimizar su dolor.
"""

# ---------- UI PRINCIPAL: 7 PREGUNTAS ----------

st.markdown("### 1️⃣ Elegí cómo querés que te hable")

with st.form("juego_oculto_form"):
    modo = st.radio(
        "¿En qué tono querés que te hable?",
        options=[
            "☕️ Modo Mate Tranqui",
            "🧢 Modo Entrenador de Vestuario",
            "⚔️ Honestidad Brutal – Modo Samurai",
            "🃏 Modo Joker – Honestidad irónica / comedia",
        ],
        index=2,
        help="Elegí desde más suave hasta samurai al hueso… o en modo Joker, con comedia.",
    )

    st.markdown("---")
    st.markdown("### 2️⃣ Respondé las 7 preguntas del Juego Oculto")

    q1 = st.text_area(
        "1) ¿Qué es lo que más te duele, te cansa o te tiene con la cabeza prendida fuego?",
        height=100,
    )

    q2 = st.text_area(
        "2) Contame una escena concreta que se repite (la película que ya te sabés de memoria).",
        height=120,
    )

    q3 = st.text_area(
        "3) Después de esa escena, ¿qué hacés casi siempre? (aunque no te guste admitirlo).",
        height=100,
    )

    q4 = st.text_area(
        "4) En esos momentos, ¿qué te decís a vos mismo? (frases, pensamientos, historia que te contás).",
        height=100,
    )

    q5 = st.text_area(
        "5) ¿Qué emociones aparecen y cómo las sentís en el cuerpo? (miedo, bronca, tristeza, culpa, mezcla… ¿y dónde se siente?).",
        height=100,
    )

    q6 = st.text_area(
        "6) Si fueras brutalmente honesto: ¿qué ganás manteniendo este juego tal como está? (aunque sea feo admitirlo).",
        height=100,
    )

    q7 = st.text_area(
        "7) Si esto siguiera igual 12 meses, ¿qué es lo que más te asusta que pase? ¿Y qué te gustaría que fuera distinto?",
        height=120,
    )

    submitted = st.form_submit_button("Ver mi juego oculto 🎭")

# ---------- LLAMADO A OPENAI Y RESPUESTA ----------

if submitted:
    if not q1.strip() or not q2.strip():
        st.warning("Necesito mínimo el dolor principal (1) y una escena concreta (2) para poder leerte bien.")
    else:
        with st.spinner("Analizando tu juego interno..."):
            user_prompt = f"""
Modo de verdad elegido por el usuario: {modo}

Respuestas del usuario a las 7 preguntas base del Juego Oculto:

1) Dolor / ruido mental actual:
\"\"\"{q1.strip()}\"\"\"

2) Escena concreta que se repite:
\"\"\"{q2.strip()}\"\"\"

3) Qué hace casi siempre después (conducta / patrón):
\"\"\"{q3.strip()}\"\"\"

4) Qué se dice por dentro (frases, historia interna):
\"\"\"{q4.strip()}\"\"\"

5) Emociones y cuerpo:
\"\"\"{q5.strip()}\"\"\"

6) Beneficio oculto de sostener este juego:
\"\"\"{q6.strip()}\"\"\"

7) Futuro: qué teme que pase si sigue igual y qué le gustaría que fuera distinto:
\"\"\"{q7.strip()}\"\"\"

Tarea:
Usá estas 7 respuestas como base para analizar el juego actual del usuario siguiendo tu metodología
(4 niveles emocionales + 12 arquetipos de juego viejo) y generá un INFORME COMPLETO siguiendo el formato
especificado en el system prompt.

Usa un lenguaje coherente con el modo elegido:
- Si el modo es Mate Tranqui, sé suave pero claro.
- Si el modo es Entrenador de Vestuario, sé directo y empático.
- Si el modo es Samurai, prioriza la honestidad brutal, sin azúcar pero sin faltar el respeto.
- Si el modo es Joker, usá humor irónico y comedia como vehículo, pero sin minimizar el dolor
  ni ridiculizar al usuario. El análisis debe seguir siendo profundo y claro.

No le pidas nada extra al usuario. Todo lo que necesitás está en estas 7 respuestas.
Inferí vos, si hace falta, en qué áreas pega este juego (dinero, relaciones, cuerpo, proyectos, etc.).

Devolvé el resultado en formato Markdown.
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.9,
                )
                output = response.choices[0].message.content

                st.markdown("---")
                st.subheader("🧾 Tu informe del Juego Oculto")
                st.markdown(output)

                st.download_button(
                    label="📥 Descargar informe (.txt)",
                    data=output,
                    file_name="juego_oculto_informe.txt",
                    mime="text/plain",
                )

            except Exception as e:
                st.error(f"Ocurrió un error al llamar a la API: {e}")

# ---------- AVISO LEGAL EN EXPANDER ----------
st.markdown("---")
with st.expander("🧾 Aviso legal y límites de El Juego Oculto"):
    st.markdown(
        """
- El Juego Oculto es una herramienta de **exploración personal y autoconocimiento**, con fines educativos.
- No constituye ni reemplaza terapia psicológica, psiquiátrica ni tratamiento médico.
- No ofrece diagnóstico, prescripción ni intervención clínica.
- Las decisiones que tomes a partir de lo que veas acá son **tu responsabilidad**.
- Si estás atravesando una crisis fuerte, ideación suicida o una situación límite,
  buscá ayuda profesional o servicios de emergencia en tu zona.
"""
    )
