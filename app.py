import streamlit as st
from scoring import evaluate_transcript

# --------------------------------------
# Streamlit Page Settings
# --------------------------------------
st.set_page_config(
    page_title="AI Student Introduction Evaluation",
    layout="wide",
    page_icon="🎤"
)

# --------------------------------------
# Header Section
# --------------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>
        🎤 AI-Powered Student Introduction Scoring Tool
    </h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>
        Evaluate communication, structure, grammar, and engagement with a single click.
    </p>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

# --------------------------------------
# Input Section Card
# --------------------------------------
st.markdown("""
<div style="
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #eee;
    margin-bottom: 20px;
">
""", unsafe_allow_html=True)

st.subheader("📝 Enter Transcript Text")

transcript_input = st.text_area(
    "Paste transcript here:",
    height=200,
    placeholder="Type or paste the student's introduction here..."
)

uploaded_file = st.file_uploader("Or upload a .txt transcript file", type=['txt'])

if uploaded_file:
    transcript_input = uploaded_file.read().decode("utf-8")
    st.success("Transcript uploaded successfully!")

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------
# Duration Section
# --------------------------------------
st.markdown("""
<div style="
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #eee;
    margin-bottom: 20px;
">
""", unsafe_allow_html=True)

st.subheader("⏱️ Audio Duration (Seconds)")

duration_seconds = st.number_input(
    "Enter audio duration in seconds (required for WPM score):",
    min_value=10,
    max_value=300,
    value=60,
    step=1
)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------
# Evaluate Button
# --------------------------------------
evaluate_btn = st.button("🔍 Evaluate Transcript", use_container_width=True)

if evaluate_btn:

    if not transcript_input.strip():
        st.error("Please enter or upload a transcript before evaluating.")

    else:
        # Spinner section
        with st.spinner("Evaluating... Please wait ⏳"):
            results = evaluate_transcript(transcript_input, duration_seconds)

        st.success("Evaluation Complete!")

        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

        # --------------------------------------
        # Overall Score Section
        # --------------------------------------
        st.subheader("📊 Overall Score")

        st.metric(
            label="Final Score (out of 100)",
            value=results["overall_score"]
        )

        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

        # --------------------------------------
        # Detailed Scoring Cards
        # --------------------------------------
        details = results["details"]

        st.subheader("🧩 Detailed Scoring Breakdown")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div style="background-color:#eef7ff; padding:15px; border-radius:10px;">
            <h4 style="color:#4A90E2;">Content & Structure</h4>
            """, unsafe_allow_html=True)
            st.write(f"• **Salutation:** {details['salutation']} / 5")
            st.write(f"• **Must-Have Keywords:** {details['keyword_must_have']} / 20")
            st.write(f"• **Good-to-Have Keywords:** {details['keyword_good_to_have']} / 10")
            st.write(f"• **Flow Structure:** {details['flow_structure']} / 5")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color:#fef6e4; padding:15px; border-radius:10px;">
            <h4 style="color:#e37a00;">Language & Delivery</h4>
            """, unsafe_allow_html=True)
            st.write(f"• **WPM Score:** {details['wpm_score']} / 10")
            st.write(f"• **Grammar Score:** {details['grammar_score']} / 10")
            st.write(f"• **Vocabulary (TTR):** {details['ttr_score']} / 10")
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div style="background-color:#e8ffe6; padding:15px; border-radius:10px;">
            <h4 style="color:#1e9f4b;">Clarity & Engagement</h4>
            """, unsafe_allow_html=True)
            st.write(f"• **Filler Word Score:** {details['filler_score']} / 15")
            st.write(f"• **Sentiment Score:** {details['sentiment_score']} / 15")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

        # --------------------------------------
        # JSON Output
        # --------------------------------------
        st.subheader("🧪 Raw JSON Output")
        st.json(results)

# --------------------------------------
# Footer Signature
# --------------------------------------
st.markdown("""
    <p style='text-align:center; color:gray; margin-top:50px;'>
        Built by <b>Miloni Halkati</b> — Nirmaan AI Internship Case Study
    </p>
""", unsafe_allow_html=True)
