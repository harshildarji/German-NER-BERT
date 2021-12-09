import pickle
import warnings

import jsonify
import numpy as np
import requests
import torch
from flask import Flask, Markup, render_template, request
from transformers import BertForTokenClassification, logging

warnings.simplefilter(action="ignore", category=Warning)
logging.set_verbosity(logging.ERROR)


print("[+] this might take a few seconds or minutes...")

app = Flask(__name__)
device = torch.device("cpu")

tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
tag_values = pickle.load(open("tag_values.pkl", "rb"))

model = BertForTokenClassification.from_pretrained(
    "bert-base-german-cased",
    num_labels=len(tag_values),
    output_attentions=False,
    output_hidden_states=False,
)
model.load_state_dict(torch.load("model.pt", map_location=device))

classes = {
    "AN": "Lawyer",
    "EUN": "European legal norm",
    "GRT": "Court",
    "GS": "Law",
    "INN": "Institution",
    "LD": "Country",
    "LDS": "Landscape",
    "LIT": "Legal literature",
    "MRK": "Brand",
    "ORG": "Organization",
    "PER": "Person",
    "RR": "Judge",
    "RS": "Court decision",
    "ST": "City",
    "STR": "Street",
    "UN": "Company",
    "VO": "Ordinance",
    "VS": "Regulation",
    "VT": "Contract",
}


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        test_sentence = str(request.form["testsentence"])

        tokenized_sentence = tokenizer.encode(test_sentence)
        input_ids = torch.tensor([tokenized_sentence])

        with torch.no_grad():
            output = model(input_ids)
        label_indices = np.argmax(output[0].numpy(), axis=2)

        tokens = tokenizer.convert_ids_to_tokens(input_ids.numpy()[0])
        new_tokens, new_labels = [], []
        for token, label_idx in zip(tokens, label_indices[0]):
            if token.startswith("##"):
                new_tokens[-1] = new_tokens[-1] + token[2:]
            else:
                new_labels.append(tag_values[label_idx])
                new_tokens.append(token)

        output = ""
        for token, label in zip(new_tokens, new_labels):
            if label != "O":
                cls = classes[label.split("-")[-1]]
                output += '<abbr title="{}"><b>{}</b><t style="color:#ff4000">[{}]</t></abbr> '.format(
                    cls, token, label
                )
            else:
                output += "{}[{}] ".format(token, label)

        output = (
            output.replace("[CLS]", "").replace("[O]", "").replace("[SEP]", "").strip()
        )
        output = output.replace(
            "[UNK]", """<abbr title="[UNK]"><b style="color:#545454">{}</b></abbr> """
        )
        output = "<strong>- Original text -</strong><br><br>{}<br><br><strong>- Analyzed text -</strong><br><br>{}<br><br><mark><strong>Tip:</strong> Hover over the red-underlined words to see its class.<mark>".format(
            test_sentence, output
        )
        return render_template("index.html", analyzed_sentence="{}".format(output))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
