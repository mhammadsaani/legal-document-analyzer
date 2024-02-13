import fitz
import numpy as np
import os
import torch
from transformers import BertTokenizer
from transformers import BertForSequenceClassification, BertTokenizer
from .constants import MODEL_PATH

model_save_path = MODEL_PATH
loaded_model = BertForSequenceClassification.from_pretrained(model_save_path)
loaded_tokenizer = BertTokenizer.from_pretrained(model_save_path)


def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)

    text = ""

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()

    return text


def predict_ndas(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    predictions = {}
    model = BertForSequenceClassification.from_pretrained(model_save_path)

    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

    input_ids = tokens["input_ids"]
    attention_mask = tokens["attention_mask"]
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=1).numpy()

    predicted_label = int(np.argmax(probabilities))

    predictions["File"] = {
        "predicted_label": predicted_label,
        "probabilities": probabilities.tolist()
    }

    return predictions

# import sys


# print(sys.argv[1])