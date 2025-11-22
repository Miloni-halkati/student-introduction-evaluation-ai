import streamlit as st
from scoring import evaluate_transcript

# --------------------------------------
# Streamlit Settings
# --------------------------------------
st.set_page_config(page_title="AI Introduction Scoring Tool", layout="wide")

st.title("🎤 Student Self-Introduction Scoring Tool")
st.write("Evaluate a student's introduction using AI-based scoring")

# --------------------------------------
# Transcript Input
# --------------------------------------
st.subheader("📄 Enter Transcript")

transcript_input = st.text_area(
    "Paste transcript here:",
    height=250,
    placeholder="Type or paste the student's introduction here..."
)

uploaded_file = st.file_uploader("Or upload a .txt transcript file", type=['txt'])

if uploaded_file:
    transcript_input = uploaded_file.read().decode("utf-8")
    st.success("Transcript uploaded successfully!")

# --------------------------------------
# Duration Input (Important for WPM)
# --------------------------------------
st.subheader("⏱️ Audio Duration (Seconds)")

duration_seconds = st.number_input(
    "Enter the audio duration in seconds (required for WPM score):",
    min_value=10,
    max_value=300,
    value=60,
    step=1
)

# --------------------------------------
# Evaluate Button
# --------------------------------------
if st.button("🔍 Evaluate Transcript"):

    if not transcript_input.strip():
        st.error("Please enter or upload a transcript before evaluating.")

    else:
        with st.spinner("Evaluating... Please wait ⏳"):
            results = evaluate_transcript(transcript_input, duration_seconds)

        st.success("Evaluation Complete!")

        # --------------------------------------
        # Display Overall Score
        # --------------------------------------
        st.subheader("📊 Overall Score")
        st.metric("Final Score (out of 100)", results["overall_score"])

        # --------------------------------------
        # Display Detailed Breakdown
        # --------------------------------------
        st.subheader("📝 Detailed Scoring Breakdown")

        details = results["details"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("### Content & Structure")
            st.write(f"Salutation Score: **{details['salutation']} / 5**")
            st.write(f"Must-Have Keywords: **{details['keyword_must_have']} / 20**")
            st.write(f"Good-to-Have Keywords: **{details['keyword_good_to_have']} / 10**")
            st.write(f"Flow Structure: **{details['flow_structure']} / 5**")

        with col2:
            st.write("### Language & Delivery")
            st.write(f"WPM Score: **{details['wpm_score']} / 10**")
            st.write(f"Grammar Score: **{details['grammar_score']} / 10**")
            st.write(f"TTR Vocabulary Score: **{details['ttr_score']} / 10**")

        with col3:
            st.write("### Clarity & Engagement")
            st.write(f"Filler Word Score: **{details['filler_score']} / 15**")
            st.write(f"Sentiment Score: **{details['sentiment_score']} / 15**")

        # --------------------------------------
        # Raw JSON Output
        # --------------------------------------
        st.subheader("🔧 Raw JSON Output")
        st.json(results)

# Footer
st.write("---")
st.write("Built by Miloni Halkati")

