import streamlit as st
import os
import random

st.set_page_config(
    page_title="for ren 🌸",
    page_icon="🌼",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Default (light mode) variables */
:root {
    --background-color: #e6e6fa;
    --text-color: #ff66cc;
    --box-bg: #fff0f5;
    --box-shadow: #ffcce6;
    --box-text: #000000;
}

/* Dark mode variables */
@media (prefers-color-scheme: dark) {
    :root {
        --background-color: #121212;
        --text-color: #ff99cc;
        --box-bg: #1e1e1e;
        --box-shadow: #ff99cc;
        --box-text: #ffffff;
    }
}

/* Apply to Streamlit container */
.stApp {
    background-color: var(--background-color);
}

/* Headline */
.headline {
    text-align: center;
    font-size: 3rem;
    font-family: Georgia, serif;
    color: var(--text-color);
    margin-bottom: 40px;
}

/* Envelope wrapper */
.envelope-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
}

/* Envelope */
.envelope {
    width: 340px;
    height: 220px;
    background: var(--box-bg);
    border-radius: 16px;
    position: relative;
    box-shadow: 0 20px 50px var(--box-shadow);
    overflow: hidden;
}

/* Envelope flap */
.flap {
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-left: 170px solid transparent;
    border-right: 170px solid transparent;
    border-top: 110px solid var(--text-color);
    transform-origin: top;
    transition: transform 0.8s ease;
    z-index: 2;
}

/* Label */
.label {
    position: absolute;
    bottom: 25px;
    width: 100%;
    text-align: center;
    font-family: Georgia, serif;
    color: var(--text-color);
    font-size: 1.2rem;
}

/* Letter animation */
.letter {
    transform: translateY(120px);
    opacity: 0;
    animation: slideUp 1s ease forwards;
}

@keyframes slideUp {
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* Card */
.card {
    background: var(--box-bg);
    padding: 40px;
    border-radius: 26px;
    text-align: center;
    box-shadow: 0 25px 60px var(--box-shadow);
    max-width: 520px;
    margin: auto;
    color: var(--box-text);
}

/* Signature animation */
.signature {
    margin-top: 24px;
    font-family: Georgia, serif;
    font-size: 1.1rem;
    color: var(--text-color);
    opacity: 0;
    animation: writeIn 2s ease forwards;
    animation-delay: 1.2s;
}

@keyframes writeIn {
    to {
        opacity: 1;
    }
}

/* Floating flowers */
.flower {
    position: fixed;
    font-size: 1.8rem;
    animation: float 6s linear infinite;
    opacity: 0.7;
    pointer-events: none;
}

@keyframes float {
    0% {
        transform: translateY(100vh) translateX(0) rotate(0deg);
    }
    50% {
        transform: translateY(50vh) translateX(20px) rotate(180deg);
    }
    100% {
        transform: translateY(-10vh) translateX(-20px) rotate(360deg);
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "opened" not in st.session_state:
    st.session_state.opened = False

# ---------------- FLOATING FLOWERS ----------------
flowers = ["🌼", "🌸", "💮"]
for _ in range(12):
    left = random.randint(0, 95)
    delay = random.uniform(0, 2)
    duration = random.randint(5, 8)
    emoji = random.choice(flowers)

    st.markdown(
        f'<div class="flower" style="left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s;">{emoji}</div>',
        unsafe_allow_html=True
    )

# ---------------- UI ----------------
st.markdown('<div class="headline">good morning sunshine ☀️</div>', unsafe_allow_html=True)

if not st.session_state.opened:
    st.markdown("""
        <div class="envelope-wrapper">
            <div class="envelope">
                <div class="flap"></div>
                <div class="label">for ren 🌸</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("💌 open envelope"):
            st.session_state.opened = True
            st.rerun()

else:
    # Autoplay music when envelope is opened
    if os.path.exists("music.mp3"):
        st.audio("music.mp3", loop=True, autoplay=True)

    st.markdown("""
        <div class="letter">
            <div class="card">
                <p style="font-size:1.35rem; line-height:1.6; font-family: Georgia, serif;">
                you make everything feel lighter without even trying <3
                everything you do matters more than you know bae
                im really glad i met you
                <br><br>
                thank you for being exactly who you are stupid btech boy💛
                </p>
                <div class="signature">
                — love always, ru
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
