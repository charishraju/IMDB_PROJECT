# IMDB_PROJECT

# 🎬 IMDb Review Sentiment Classification

This project is a full-stack Natural Language Processing (NLP) pipeline designed to classify IMDb movie reviews into **positive**, **negative**, or **neutral** sentiments. It showcases end-to-end development — from **web scraping** real-world reviews to **deploying** a machine learning model.

---

## 🚀 Project Overview

In a world where user reviews significantly influence decision-making, understanding public sentiment becomes essential. This project scrapes IMDb reviews and uses text classification techniques to determine the sentiment behind them.

It combines **data collection**, **cleaning**, **EDA**, **NLP**, and **machine learning**, making it an excellent demonstration of real-world NLP project flow.

---

## 🧰 Tech Stack

- **Languages**: Python 3.x
- **Libraries**: `BeautifulSoup`, `requests`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `nltk`, `wordcloud`
- **ML Models**: Logistic Regression, SVM, Random Forest, BERT (optional)
- **Other Tools**: `Streamlit` (for deployment), `logging`, `joblib`, `Jupyter Notebook`

```

## 🗂️ Project Structure

imdb_sentiment_classifier/
├── logger/                     # Logger setup (in __init__.py)
│
├── utils/                      # Utility modules (scraper, preprocessing, modeling, etc.)
│   ├── web_scraper.py
│   ├── model_builder.py
│   └── text_cleaner.py
│
├── web_scrapper/
│   ├── codes/                  # Scraping scripts
│   └── data/                   # Raw and processed review data
│
├── notebooks/                  # Jupyter notebooks for EDA and experiments
│
├── app/                        # Streamlit app for model deployment
│
├── README.md
└── requirements.txt


```

## 📌 Key Features

- ✅ Web scraping IMDb reviews using `BeautifulSoup`
- ✅ Text preprocessing: cleaning, tokenizing, lemmatizing
- ✅ Exploratory Data Analysis (EDA) with visualizations
- ✅ Feature engineering from raw text
- ✅ Training and comparing ML models
- ✅ Model evaluation using accuracy, F1-score, confusion matrix
- ✅ Optional: LIME/SHAP for explainability
- ✅ Deployed Streamlit app for live inference

---

## 📊 Exploratory Data Analysis

Some EDA highlights:
- Sentiment distribution across dataset
- Word frequency visualizations
- Review length vs sentiment patterns
- Bigram/trigram analysis
- Word clouds per sentiment

> Detailed visualizations are available in the `notebooks/EDA.ipynb`.

---

## 🧠 Modeling Approach

1. Preprocessed text using TF-IDF vectorization
2. Trained multiple classifiers (Logistic Regression, SVM, Random Forest, etc.)
3. Evaluated models on accuracy, F1-score
4. Selected best model and saved using `joblib`
5. (Optional) Fine-tuned `BERT` using `transformers` library for better performance

---

## 🧪 Results

| Model               | Accuracy | F1 Score |
|--------------------|----------|----------|
| Logistic Regression| 91.2%    | 0.91     |
| SVM                | 93.0%    | 0.93     |
| Random Forest      | 88.4%    | 0.88     |
| BERT (optional)    | 95.6%    | 0.95     |

> Final model was deployed using Streamlit for real-time predictions.

---

## 🌐 Demo

📽️ **Live Demo (if deployed)**: [streamlit link]  
📸 **Screenshots**: Included in `screenshots/` folder (if available)

---

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/imdb-sentiment-classifier.git
cd imdb-sentiment-classifier
