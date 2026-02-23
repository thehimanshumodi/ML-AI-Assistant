# app.py

import streamlit as st
import time
from llm import generate_answer

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="ML AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# ==============================
# CUSTOM CSS (SaaS Style)
# ==============================

st.markdown("""
<style>

/* Global spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Top Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
}

/* Gradient Title */
.title-gradient {
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(90deg, #6366F1, #22D3EE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Status Badge */
.status-badge {
    padding: 6px 12px;
    border-radius: 20px;
    background-color: #1F2937;
    font-size: 13px;
    color: #22D3EE;
}

/* Hide footer */
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ==============================
# NAVBAR
# ==============================

st.markdown("""
<div class="navbar">
    <div class="title-gradient">Machine Learning AI Assistant</div>
    <div class="status-badge">● System Ready</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==============================
# SIDEBAR DASHBOARD
# ==============================

with st.sidebar:
    st.markdown("## ⚙️ Dashboard")
    st.markdown("**Model:** Groq LLM")
    st.markdown("**Retrieval:** FAISS + BM25")
    st.markdown("**Domain:** Machine Learning")

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Built by Himanshu Modi")

# ==============================
# SESSION STATE
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# CHAT DISPLAY
# ==============================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==============================
# USER INPUT
# ==============================

prompt = st.chat_input("Ask a machine learning question...")

if prompt:

    prompt = prompt.strip()

    if prompt == "":
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing documents..."):

            try:
                start_time = time.time()

                answer, sources = generate_answer(prompt)

                response_time = round(time.time() - start_time, 2)

                st.markdown(answer)
                st.caption(f"⏱ Response time: {response_time} sec")

                if sources:
                    with st.expander("📄 Retrieved Sources"):
                        for i, doc in enumerate(sources):
                            st.markdown(f"**Source {i+1}**")
                            st.write(doc.page_content.strip())

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error("Something went wrong.")
                st.write(str(e))