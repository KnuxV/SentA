"""
Created by kevin-desktop, on the 18/02/2023
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
from transformers import pipeline
from tqdm import tqdm

# Load Aspect-Based Sentiment Analysis model
absa_tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
absa_model = AutoModelForSequenceClassification \
    .from_pretrained("yangheng/deberta-v3-base-absa-v1.1")

# Load a traditional Sentiment Analysis model
sentiment_model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_model = pipeline("sentiment-analysis", model=sentiment_model_path,
                           tokenizer=sentiment_model_path)


def run_asba_model(txt, aspect, pbar=None):
    asp = aspect
    inputs = absa_tokenizer(f"[CLS] {txt} [SEP] {asp} [SEP]", return_tensors="pt")
    outputs = absa_model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)
    probs = probs.detach().numpy()[0]
    if pbar is not None:
        pbar.update(1)
    return tuple(probs)
    # return ", ".join([str(val.round(2)) for val in probs])


def run_regular_model(txt):
    return sentiment_model([txt])


def run_models(txt, lst_of_terms):
    dic_conversion = {0: "Neg: ", 1: "Neu: ", 2: "Pos: "}
    # dic = {term: [] for term in lst_of_terms}
    lst = []
    for term in lst_of_terms:
        lst_sent = [dic_conversion[ind] + str(val.round(2)) for ind, val in enumerate(list(run_asba_model(txt, term)))]
        if term == "":
            lst.append(["avg"] + lst_sent)
        else:
            lst.append([term] + lst_sent)
    # lst.append(['overall'] + list(run_regular_model(txt)))
    return lst
