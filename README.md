# 📰 Fake News Detector

An AI-powered web application built with a fine-tuned DistilBERT model to classify news articles as REAL or FAKE. This project demonstrates an end-to-end machine learning workflow, from data cleaning and model training to deployment as an interactive app using Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL_HERE)

## ✨ Features
- **Interactive UI**: A clean and simple user interface built with Streamlit.
- **AI-Powered Classification**: Utilizes a powerful `DistilBERT` model fine-tuned on a large dataset of news articles.
- **Real-time Predictions**: Paste any news article and get an instant prediction with a corresponding confidence score.
- **Data Leakage Prevention**: The training process specifically addresses and cleans data leakage issues for a more robust and reliable model.

## 🛠️ Technologies Used
- **Backend & Modeling**: Python, PyTorch, Transformers (Hugging Face), Scikit-learn, Pandas
- **Frontend & Deployment**: Streamlit, Streamlit Community Cloud
- **Version Control**: Git, GitHub, Git LFS

## 📂 Project Structure
```
Fake-News-Detector/
├── app.py                  # The main Streamlit application script
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level dependencies for deployment
├── model/
│   └── final_fake_news_model_fixed/  # Saved model files
├── data/
│   └── ... (Raw CSV data files)
├── notebooks/
│   └── fake_news_detection.ipynb   # Jupyter Notebook for experimentation
└── README.md
```

## 🚀 Running Locally
To run this project on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Shiva2806/Fake-News-Detector.git](https://github.com/Shiva2806/Fake-News-Detector.git)
   cd Fake-News-Detector
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   The application should open in your web browser.

##  acknowledgments
The training data for this model is primarily based on a public Kaggle dataset containing real and fake news. To enhance the model's robustness, this was augmented with a manually curated dataset of 1,000 additional articles (500 real and 500 fake).
