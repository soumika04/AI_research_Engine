import streamlit as st
from core.pdf_processor import extract_text_from_pdf
from core.gap_analyzer import analyze_single_paper, analyze_cross_papers
from ui.styles import apply_custom_styles
import time

st.set_page_config(
    page_title="Research Intelligence Engine",
    layout="wide"
)

st.markdown(apply_custom_styles(), unsafe_allow_html=True)

st.markdown('<div class="title">AI Research Intelligence Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Quantized Mistral 7B • Multi-Document Academic Analysis</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("System Settings")
    chunk_limit = st.slider("Chunks per Paper", 1, 4, 2)
    st.success("Model: mistral:7b-instruct-q4_0 (Quantized)")
    st.info("Running Locally via Ollama")

uploaded_files = st.file_uploader(
    "Upload Research Papers (PDF)",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    analyses = []

    col1, col2, col3 = st.columns(3)
    col1.metric("Documents", len(uploaded_files))
    col2.metric("Model", "Mistral 7B Q4")
    col3.metric("Mode", "Comparative Analysis")

    st.markdown("---")

    for file in uploaded_files:
        with st.spinner(f"Analyzing {file.name}..."):
            text = extract_text_from_pdf(file)
            analysis = analyze_single_paper(text, chunk_limit)
            analyses.append(analysis)

        with st.expander(f"{file.name} Analysis"):
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            st.write(analysis)
            st.markdown('</div>', unsafe_allow_html=True)

    if len(analyses) > 1:
        st.markdown("## Cross-Paper Intelligence")

        with st.spinner("Detecting Research Gaps..."):
            time.sleep(1)
            gap_result = analyze_cross_papers(analyses)

        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("### Identified Research Gaps & Opportunities")
        st.write(gap_result)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.warning("Upload at least one research paper to begin.")