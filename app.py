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
### ¿Qué hace este juego?
1. Entrás con un problema real (plata, tiempo, vínculos, etc.).
2. El sistema lee tu historia y te muestra **el juego viejo** que estás jugando.
3. Te devuelve un **informe** con:
   - tu patrón,
   - el juego oculto (reglas, miedos, beneficio),
   - y **primeros pasos concretos** para jugar un juego nuevo.

---
"""
)

# ---------- INICIALIZAR CLIENTE OPENAI ----------
# Importante: en Streamlit Cloud tenés que cargar tu clave en:
# Settings → Secrets → {"OPENAI_API_KEY": "tu_clave_aca"}
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

———————— FORMATO DEL INFORME ————————

Siempre devolvés un informe estructurado en este formato (en español, claro y directo):

# 🔍 Dolor principal de hoy
- Resumen breve del dolor actual, con las palabras del usuario.
- Área principal donde pega (ej: dinero/tiempo, pareja, vínculos, cuerpo, propósito, etc.).

# 🎭 Juego viejo que estás jugando
- Nombre irónico del juego (ej: “Campeón Mundial del Último Minuto”).
- Nombre serio entre paréntesis.
- Versión personalizada usando una frase textual del usuario.
- 1 frase que resuma el juego viejo en lenguaje cotidiano.

# 🧩 Radiografía en 4 niveles
## 1. Disparadores
- Lista simple de disparadores típicos.

## 2. Interpretaciones (la película que te contás)
- Frases clave que el usuario se dice a sí mismo.
- Una frase “núcleo” que sostenga el juego.

## 3. Emoción y cuerpo
- Emoción principal (miedo, bronca, etc.).
- Cómo se siente en el cuerpo.

## 4. Conducta / patrón
- Qué hace casi siempre después, en términos concretos.

# 🕳️ Juego oculto: reglas, miedos y beneficio
## Reglas invisibles
- 2 a 4 reglas internas no declaradas.

## Miedos que este juego protege
- 1 a 3 miedos de fondo.

## Beneficio oculto
- Qué gana el usuario manteniendo este juego (aunque le cueste).

# 🎮 Nuevo juego posible
- Nombre del nuevo juego (positivo, concreto, sin new-age vacío).
- Breve descripción del nuevo juego.
- 2–4 nuevas reglas fáciles de recordar.

# 🚶 Primeros pasos (micro-movimientos)
- 2–3 acciones específicas para los próximos 7 días.
- 1 conversación incómoda o decisión concreta, si aplica.

# 🧾 Aviso legal breve
- Recordatorio de que esto es reflexión, no diagnóstico ni terapia.

Tono general:
- Claro, directo, humano.
- Con una dosis de humor irónico cuando ayuda a que el usuario se ría de su propio juego,
  sin humillarlo ni minimizar su dolor.
"""

# ---------- UI PRINCIPAL ----------

st.markdown("### 1️⃣ Elegí cómo querés que te hable")

with st.form("juego_oculto_form"):
    modo = st.radio(
        "¿En qué tono querés que te hable?",
        options=[
            "☕️ Modo Mate Tranqui",
            "🧢 Modo Entrenador de Vestuario",
            "⚔️ Honestidad Brutal – Modo Samurai",
        ],
        index=2,
        help="Elegí desde más suave hasta samurai al hueso.",
    )

    st.markdown("---")
    st.markdown("### 2️⃣ ¿Dónde te aprieta más el zapato hoy?")

    area = st.selectbox(
        "Área principal donde sentís el quilombo:",
        [
            "Dinero / trabajo / decisiones económicas",
            "Tiempo / foco / organización",
            "Pareja / intimidad",
            "Familia / hijos / vínculos cercanos",
            "Amistades / vida social",
            "Cuerpo / energía / salud",
            "Propósito / proyecto de vida",
            "Autoestima / narrativa interna",
            "Otra / mezcla rara",
        ],
    )

    st.markdown("---")
    st.markdown("### 3️⃣ Contame el dolor y la película que se repite")

    dolor = st.text_area(
        "¿Qué es lo que más te duele o te cansa de esta situación?",
        height=120,
        placeholder="Ej: Siempre llego con lo justo con la plata; vivo apagando incendios y no termino de ordenar nada...",
    )

    escena = st.text_area(
        "Contame una escena concreta que se repita (la película que ya te sabés de memoria)",
        height=140,
        placeholder="Ej: Llega la fecha del alquiler, miro la cuenta y otra vez estoy al límite...",
    )

    st.markdown("---")
    st.markdown("### 4️⃣ Algo más que quieras aclarar (opcional)")

    extra = st.text_area(
        "Contexto, personas involucradas, cómo reaccionás, qué ya intentaste, etc. (opcional)",
        height=100,
        placeholder="Si no tenés nada más para agregar, podés dejar esto vacío.",
    )

    submitted = st.form_submit_button("Ver mi juego oculto 🎭")

# ---------- LLAMADO A OPENAI Y RESPUESTA ----------

if submitted:
    if not dolor.strip() or not escena.strip():
        st.warning("Necesito al menos el dolor principal y una escena concreta para poder leerte bien.")
    else:
        with st.spinner("Analizando tu juego interno..."):
            user_prompt = f"""
Modo de verdad elegido por el usuario: {modo}

Área principal de dolor: {area}

Dolor principal (palabras del usuario):
\"\"\"{dolor.strip()}\"\"\"

Escena concreta que se repite:
\"\"\"{escena.strip()}\"\"\"

Información adicional aportada:
\"\"\"{extra.strip()}\"\"\"

Tarea:
Analiza esta información siguiendo tu metodología (4 niveles emocionales + 12 arquetipos de juego viejo)
y genera un INFORME COMPLETO siguiendo el formato especificado en el system prompt.

Usa un lenguaje coherente con el modo elegido:
- Si el modo es Mate Tranqui, sé suave pero claro.
- Si el modo es Entrenador de Vestuario, sé directo y empático.
- Si el modo es Samurai, prioriza la honestidad brutal, sin azúcar pero sin faltar el respeto.

Devuelve el resultado en formato Markdown.
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.7,
                )
                output = response.choices[0].message.content

                st.markdown("---")
                st.subheader("🧾 Tu informe del Juego Oculto")
                st.markdown(output)

                # ---------- BOTÓN DE DESCARGA ----------
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
