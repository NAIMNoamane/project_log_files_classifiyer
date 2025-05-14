from regex_processor import classify_with_regex
from Bert_processor import classify_with_bert
from Deepseek_processor import classify_with_llm
import pandas as pd



def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels

def classify_log(source, log_msg):
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if not label:
            label = classify_with_bert(log_msg)
    return label

def main(input_file):

    df = pd.read_csv(input_file)

     # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    output_file = "output.csv"
    df.to_csv(output_file)