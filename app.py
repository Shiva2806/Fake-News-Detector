# app.py (Polished Version)
import streamlit as st
from transformers import pipeline
import torch

# --- Page Configuration (set this at the top) ---
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"  # Use the wide layout
)

# --- Model Loading (cached for performance) ---
@st.cache_resource
def load_model():
    model_path = "./model/final_fake_news_model_fixed"
    device = 0 if torch.cuda.is_available() else -1
    pipe = pipeline("text-classification", model=model_path, device=device)
    return pipe

pipe = load_model()


# --- Sidebar Content ---
with st.sidebar:
    st.title("About")
    st.info(
        "This is a fake news detector built using a fine-tuned DistilBERT model. "
        "It was trained on a dataset of real and fake news articles to learn the "
        "stylistic differences between them."
    )
    with st.expander("How it works"):
        st.write(
            "The model analyzes the text for patterns, tone, and language commonly "
            "found in either legitimate news reporting or sensationalized/fake articles. "
            "Paste your text on the right and click 'Analyze News' to see the result."
        )


# --- Main Page Content ---
st.title("📰 Fake News Detector")
st.write("Enter the text of a news article below to check if it's REAL or FAKE.")

# Create two columns for the layout
col1, col2 = st.columns([2, 1])  # Make the first column twice as wide as the second

with col1:
    user_input = st.text_area("Enter News Article Text:", height=300)

with col2:
    st.subheader("Analysis Result")
    # Add a placeholder for the result
    result_placeholder = st.empty()
    result_placeholder.info("The prediction will appear here.")


# Create a button that fills the width of the first column
if st.button("Analyze News", use_container_width=True):
    if user_input:
        with st.spinner("Analyzing..."):
            result = pipe(user_input)[0]
            label_map = {'LABEL_1': 'REAL', 'LABEL_0': 'FAKE'}
            predicted_label = label_map[result['label']]
            confidence = result['score']

            if predicted_label == 'REAL':
                result_placeholder.success(f"Prediction: REAL (Confidence: {confidence:.2%})")
            else:
                result_placeholder.error(f"Prediction: FAKE (Confidence: {confidence:.2%})")
    else:
        st.warning("Please enter some text to analyze.")