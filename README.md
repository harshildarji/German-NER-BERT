# German NER on Legal Data using BERT

This project consist of the following tasks:
1. Fine-tune German BERT on Legal Data,
2. Create a minimal front-end that accepts a German sentence and shows its NER analysis.

## 1. Fine-tune German BERT on Legal Data

- The entire process of fine-tuning German BERT on Legal Data is available in [german_bert_ner.ipynb](https://github.com/harshildarji/German-NER-BERT/blob/main/german_bert_ner.ipynb).
- This notebook also contains abstract descriptions whenever deemed necessary.

## 2. Execute the minimal front-end

To run this project on **`localhost`**, follow these simple steps:

1. Create a virtual enviroment using:
```bash
conda create -n german_bert_ner python=3.9
```

2. Activate this virtual enviroment:
```bash
conda activate german_bert_ner
```

3. Clone this repo:
```bash
git clone https://github.com/harshildarji/German-NER-BERT.git
```

4. **`cd`** to repo:
```bash
cd German-NER-BERT
```

5. Install required packages using:
```bash
pip3 install -r requirements.txt
```

6. Next, we need three important files; **`model.pt`**, **`tag_values.pkl`**, and **`tokenizer.pkl`**. One can either generate these files by executing through [german_bert_ner.ipynb](https://github.com/harshildarji/German-NER-BERT/blob/main/german_bert_ner.ipynb) which will take **45-60 minutes** or **download** the latest versions of these files from **my DropBox** using:
```bash
wget https://www.dropbox.com/s/vos8pqwmlbqe0wf/model.pt
wget https://www.dropbox.com/s/u2oojgmmprt0a9d/tag_values.pkl
wget https://www.dropbox.com/s/uj15pab78emefoq/tokenizer.pkl
```

7. Once above-mentioned files are generated/downloaded, run **`app.py`** as:
```bash
python3 app.py
```

8. Once **`app.py`** is successfully executed, head over to **`http://localhost:5000/`**.

9. In the provided **text-area**, input a German (*law*) sentence, for example: ***`1. Das Bundesarbeitsgericht ist gemäß § 9 Abs. 2 Satz 2 ArbGG iVm. § 201 Abs. 1 Satz 2 GVG für die beabsichtigte Klage gegen den Bund zuständig .`***

10. Final output:

![German BERT NER Example](https://i.imgur.com/0JzbBci.gif)

## References:

1. Leitner, Elena, Georg Rehm, and Julián Moreno-Schneider. "A dataset of german legal documents for named entity recognition." _arXiv preprint arXiv:2003.13016_ (2020).
