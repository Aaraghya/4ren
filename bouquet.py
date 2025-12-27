import streamlit as st

st.set_page_config(
    page_title="for ren 🌸",
    page_icon="🌼",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f6c1d1, #d6c6ff);
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.envelope {
    width: 280px;
    height: 180px;
    background: #fbe3ec;
    position: relative;
    border-radius: 12px;
    cursor: pointer;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}

.envelope:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-left: 140px solid transparent;
    border-right: 140px solid transparent;
    border-top: 90px solid #f3b6c8;
    border-radius: 12px;
}

.label {
    position: absolute;
    bottom: 20px;
    width: 100%;
    text-align: center;
    font-family: Georgia, serif;
    color: #7a3e6c;
    font-size: 1.1rem;
}

.card {
    background: #fff;
    padding: 35px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 20px 50px rgba(0,0,0,0.18);
    max-width: 320px;
}

.flowers {
    font-size: 2.2rem;
    margin-bottom: 15px;
}

.message {
    font-size: 1.4rem;
    font-family: 'Georgia', serif;
    color: #5a2a5f;
    line-height: 1.5;
}

.from {
    margin-top: 20px;
    font-size: 1rem;
    color: #8b5fa6;
}
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "opened" not in st.session_state:
    st.session_state.opened = False

# ---------- UI ----------
st.markdown('<div class="container">', unsafe_allow_html=True)

if not st.session_state.opened:
    if st.button("💌 open envelope"):
        st.session_state.opened = True

    st.markdown("""
        <div class="envelope">
            <div class="label">for ren 🌼</div>
        </div>
    """, unsafe_allow_html=True)

else:
    # Music starts AFTER interaction
   # st.audio("music.mp3", loop=True)

    st.markdown("""
        <div class="card">
            <div class="flowers">🌼 🌸 🌼</div>
            <div class="message">
                you make things lighter without trying,<br>
                love you the most.
            </div>
            <div class="from">
                — love always, ru 💗
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
