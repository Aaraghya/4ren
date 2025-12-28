import streamlit as st
import os

st.set_page_config(
    page_title="for ren 🌸",
    page_icon="🌼",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Light mode variables */
@media (prefers-color-scheme: light) {
    :root {
        --background-color: #e6e6fa;
        --text-color: #ff66cc;
        --box-bg: #fff0f5;
        --box-shadow: #ffcce6;
        --box-text: #000000;
    }
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

body {
    background-color: var(--background-color);
}

/* Center everything */
.main {
    display: flex;
    justify-content: center;
    align-items: center;
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
    transition: transform 0.4s ease;
}

.envelope:hover {
    transform: translateY(-6px);
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

.envelope.open .flap {
    transform: rotateX(180deg);
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

/* Floating daisies */
.daisy {
    position: fixed;
    font-size: 2rem;
    animation: float 6s linear infinite;
    opacity: 0.8;
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

/* Center button */
div[data-testid="column"] button {
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "opened" not in st.session_state:
    st.session_state.opened = False

# ---------------- FLOATING DAISIES ----------------
import random
for i in range(15):
    delay = random.uniform(0, 3)
    left_pos = random.randint(0, 95)
    duration = random.randint(5, 8)
    st.markdown(
        f'<div class="daisy" style="left:{left_pos}%; animation-delay:{delay}s; animation-duration:{duration}s;">🌼</div>',
        unsafe_allow_html=True
    )

# ---------------- UI ----------------
st.markdown('<div class="headline">good morning sunshine☀️</div>', unsafe_allow_html=True)

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
    # Safe audio (won't crash if missing)
    if os.path.exists("music.mp3"):
        st.audio("music.mp3", loop=True)

    st.markdown("""
        <div class="card">
            <p style="font-size:1.35rem; line-height:1.6; font-family: Georgia, serif;">
            i'm so grateful for you & everything u bring.
            you make everything better just by being you. 
            <br><br>
            thank you for all the little things aryan. 💕          
            </p>
            <p style="margin-top:20px; color:var(--text-color);">
            — love always, ru
            </p>
        </div>
    """, unsafe_allow_html=True)
