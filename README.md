# 📰 Fake News Detector

An AI-powered web application built with a fine-tuned DistilBERT model, now enhanced with **Google's Gemini API**, to classify news articles as REAL or FAKE. This project demonstrates an end-to-end machine learning workflow, from data cleaning and model training to deployment as an interactive app using Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fake-news-detector-kb8r6pdrcnaehaegbebefx.streamlit.app/)

---

## 📸 Application Screenshot

Here's a glimpse of the Fake News Detector in action:

![Fake News Detector App Screenshot](https://raw.githubusercontent.com/Shiva2806/Fake-News-Detector/assets/Demo.png)


---

## ✨ Features

-   **Interactive UI**: A clean and simple user interface built with Streamlit.
-   **Advanced AI-Powered Classification**: Utilizes a powerful `DistilBERT` model fine-tuned on a large dataset, further bolstered by the sophisticated natural language understanding and fact-checking capabilities of **Google's Gemini API**.
-   **Real-time Predictions**: Paste any news article and get an instant prediction with a corresponding confidence score.
-   **Data Leakage Prevention**: The training process specifically addresses and cleans data leakage issues for a more robust and reliable model.

---

## 🛠️ Technologies Used

-   **Backend & Modeling**: Python, PyTorch, Transformers (Hugging Face), Scikit-learn, Pandas
-   **AI Integration**: Google Gemini API
-   **Frontend & Deployment**: Streamlit, Streamlit Community Cloud
-   **Version Control**: Git, GitHub, Git LFS

---

## 📂 Project Structure
Ah, I see! My apologies again for the misunderstanding. You want the entire content of the README.md that I previously generated, presented as a single block of text (or "cell") so you can easily copy and paste it into your README.md file.

Here is the complete README.md content, ready for you to copy-paste:

Markdown

# 📰 Fake News Detector

An AI-powered web application built with a fine-tuned DistilBERT model, now enhanced with **Google's Gemini API**, to classify news articles as REAL or FAKE. This project demonstrates an end-to-end machine learning workflow, from data cleaning and model training to deployment as an interactive app using Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fake-news-detector-kb8r6pdrcnaehaegbebefx.streamlit.app/)

---

## 📸 Application Screenshot

Here's a glimpse of the Fake News Detector in action:

![Fake News Detector App Screenshot](https://raw.githubusercontent.com/Shiva2806/Fake-News-Detector/main/docs/app_screenshot.png)
*(**Note**: Please replace `https://raw.githubusercontent.com/Shiva2806/Fake-News-Detector/main/docs/app_screenshot.png` with the actual public URL or relative path to your screenshot after you've added it to your repository. A common practice is to create a `docs` or `images` folder in your project root and place the screenshot there.)*

---

## ✨ Features

-   **Interactive UI**: A clean and simple user interface built with Streamlit.
-   **Advanced AI-Powered Classification**: Utilizes a powerful `DistilBERT` model fine-tuned on a large dataset, further bolstered by the sophisticated natural language understanding and fact-checking capabilities of **Google's Gemini API**.
-   **Real-time Predictions**: Paste any news article and get an instant prediction with a corresponding confidence score.
-   **Data Leakage Prevention**: The training process specifically addresses and cleans data leakage issues for a more robust and reliable model.

---

## 🛠️ Technologies Used

-   **Backend & Modeling**: Python, PyTorch, Transformers (Hugging Face), Scikit-learn, Pandas
-   **AI Integration**: Google Gemini API
-   **Frontend & Deployment**: Streamlit, Streamlit Community Cloud
-   **Version Control**: Git, GitHub, Git LFS

---

## 📂 Project Structure

Fake-News-Detector/
├── app.py                      # The main Streamlit application script
├── requirements.txt            # Python dependencies
├── packages.txt                # System-level dependencies for deployment
├── .streamlit/                 # Streamlit specific configuration and secrets
│   └── secrets.toml            # Stores API keys and other secrets (NOT to be committed)
├── model/
│   └── final_fake_news_model_fixed/  # Saved model files
├── data/
│   └── ... (Raw CSV data files)
├── notebooks/
│   └── fake_news_detection.ipynb     # Jupyter Notebook for experimentation
├── docs/                       # New folder for documentation assets like screenshots
│   └── app_screenshot.png      # Your application screenshot (Suggested location)
└── README.md


---

## 🚀 Running Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shiva2806/Fake-News-Detector.git](https://github.com/Shiva2806/Fake-News-Detector.git)
    cd Fake-News-Detector
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the environment:**
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your Google Gemini API Key:**
    The application requires a Google Gemini API key to function. **Crucially, never hardcode your API key directly into your `app.py` or commit it to your public repository.** Follow these secure practices:

    * **Local Development:**
        Create a folder named `.streamlit` in your project's root directory (if it doesn't already exist). Inside `.streamlit`, create a file named `secrets.toml`. Add your Gemini API key to this file like so:
        ```toml
        GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
        ```
        Replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual Gemini API key. Make sure to add `.streamlit/secrets.toml` to your `.gitignore` file to prevent it from being committed to your repository.

    * **Streamlit Community Cloud Deployment:**
        When deploying to Streamlit Community Cloud, you can securely add your API key through the app's settings. Go to your app's dashboard on Streamlit Community Cloud, navigate to "Advanced settings" or "Secrets," and paste the content of your `secrets.toml` file (i.e., `GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"`). Streamlit will then make this available to your application via `st.secrets`.

    You can obtain a Google Gemini API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

6.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The application should open in your web browser.

---

##  Acknowledgments

The training data for this model is primarily based on a public Kaggle dataset containing real and fake news. To enhance the model's robustness, this was augmented with a manually curated dataset of 1,000 additional articles (500 real and 500 fake). The integration with Google's Gemini API has further significantly improved the model's accuracy and capabilities.

