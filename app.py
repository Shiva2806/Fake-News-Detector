# app.py — Fake News Detector with Gemini Verification

import streamlit as st
from transformers import pipeline
import torch
import google.generativeai as genai

# --- Page Setup ---
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="wide")

# --- Load ML Model ---
@st.cache_resource
def load_model():
    model_path = "./model/final_fake_news_model_fixed"
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("text-classification", model=model_path, device=device)

pipe = load_model()

# --- Configure Gemini ---
genai.configure(api_key="AIzaSyAqP57CRym2ehHvnu5RtOwedJuhlz9viyM")

# --- Gemini Fact Checker ---
def verify_with_gemini(query):
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        prompt = f"""
        Fact check this news article and determine whether it's likely REAL or FAKE:

        "{query}"

        Return a verdict (REAL or FAKE) and a short explanation.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

# --- Sidebar Info ---
with st.sidebar:
    st.title("About")
    st.info(
        "This app uses a fine-tuned DistilBERT model to predict whether a news article is REAL or FAKE. "
        "It also checks factual accuracy using Google's Gemini AI."
    )
    with st.expander("How It Works"):
        st.markdown(
            "- **BERT**: Checks the writing pattern and language tone.\n"
            "- **Gemini**: Validates facts and provides a short explanation."
        )

# --- Main UI ---
st.title("📰 Fake News Detector")
st.write("Paste a news article below to check if it's real or fake, with AI-powered verification.")

col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Enter News Article Text:", height=300)

with col2:
    st.subheader("Analysis Result")
    result_placeholder = st.empty()
    factcheck_placeholder = st.empty()

# --- Analyze Button ---
if st.button("Analyze News", use_container_width=True):
    if user_input:
        # BERT prediction
        with st.spinner("Analyzing with ML model..."):
            result = pipe(user_input)[0]
            label_map = {'LABEL_1': 'REAL', 'LABEL_0': 'FAKE'}
            label = label_map[result["label"]]
            confidence = result["score"]

            if label == "REAL":
                result_placeholder.success(f"Prediction: REAL ({confidence:.2%})")
            else:
                result_placeholder.error(f"Prediction: FAKE ({confidence:.2%})")

        # Gemini fact-checking
        with st.spinner("Fact-checking with Gemini..."):
            st.markdown("---")
            st.subheader("🤖 Gemini AI Fact-Check")
            gemini_result = verify_with_gemini(user_input)
            factcheck_placeholder.markdown(gemini_result)
    else:
        st.warning("Please enter some text first.")
