# NLP Pipeline for Redaction and Classification

This project implements a complete Natural Language Processing (NLP) pipeline to:

- Preprocess and clean raw text data
- Automatically redact sensitive information such as names and emails
- Train a text classifier to categorize documents

The structure is modular and designed for clarity, scalability, and real-world use.

## Project Structure

```
.
├── raw_data/         # Original dataset
├── data/             # Cleaned and processed data
├── models/           # Saved machine learning models
├── scripts/          # Python scripts for each pipeline step
├── .venv/            # Virtual environment
├── requirements.txt  # Python dependencies
└── README.md         # Project overview
```

## Pipeline Overview

1. Data Loading  
   Load raw text data from CSV or other formats.

2. Preprocessing  
   Clean text by removing punctuation, converting to lowercase, tokenizing, etc.

3. Redaction  
   Detect and mask sensitive entities using spaCy or regular expressions.

4. Vectorization  
   Convert text to numerical features using TF-IDF or word embeddings.

5. Classification  
   Train a model such as Logistic Regression or Support Vector Machine to classify text.

6. Evaluation  
   Measure model performance using accuracy, precision, recall, and F1-score.

## Installation

```bash
# Clone the repository
git clone https://github.com/colombe-tolokin/nlp-redaction-classification.git
cd nlp-redaction-classification

# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## Dataset

This project uses the [News Articles Classification Dataset](https://www.kaggle.com/datasets/banuprakashv/news-articles-classification-dataset-for-nlp-and-ml) from Kaggle. It contains a comprehensive collection of articles across five news categories with detailed content. Download the dataset and place it in the `raw_data/` folder.

## Running the Pipeline

Each step is modularized in the `scripts/` folder. Example usage:

```bash
python scripts/preprocess.py
python scripts/redact.py
python scripts/train_classifier.py
```

## Sample Results

- Redaction accuracy: 92 percent
- Classification F1-score: 0.87
- Model: Logistic Regression with TF-IDF features

## Future Improvements

- Integrate deep learning models such as BERT
- Develop a web interface for document upload and redaction
- Enhance entity recognition with custom named entity models

## Contributing

Pull requests are welcome. For major changes, please open an issue to discuss proposed modifications.

## License

This project is licensed under the MIT License.


