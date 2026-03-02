# Named Entity Recognition (NER) using spaCy

This project demonstrates a simple **Named Entity Recognition (NER)** pipeline using **spaCy** in Python. It extracts named entities from text, explains their labels, visualizes them, and saves the results to a CSV file.

---

## 📌 Features

* Uses spaCy's pretrained English model `en_core_web_sm`
* Extracts named entities such as:

  * Organizations
  * People
  * Dates
  * Locations
  * Monetary values
* Displays entity label explanations
* Visualizes entities using **displaCy**
* Exports extracted entities to a CSV file

---

## 🛠️ Technologies Used

* Python 3.x
* spaCy
* pandas
* IPython (for visualization support)

---

## 📂 Project Structure

```
name_entity_recognition/
│
├── main.py                  # Main Python script
├── extracted_entities.csv   # Output CSV file (generated)
├── README.md                # Project documentation
└── .venv/                   # Virtual environment (optional)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 2️⃣ Install required dependencies

```bash
pip install spacy pandas ipython
```

### 3️⃣ Download spaCy English model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Run

```bash
python main.py
```

After running:

* Named entities will be printed in the terminal
* A file `extracted_entities.csv` will be generated
* Entity visualization will render in Jupyter/IPython-supported environments

---

## 🧠 Sample Output

| Entity        | Label  | Explanation                       |
| ------------- | ------ | --------------------------------- |
| Amazon        | ORG    | Companies, agencies, institutions |
| Andy Jassy    | PERSON | People, including fictional       |
| July 30, 2023 | DATE   | Absolute or relative dates        |
| $4 billion    | MONEY  | Monetary values                   |
| Paris         | GPE    | Countries, cities, states         |

---


## 📜 License

This project is open-source and free to use for educational purposes.

---

⭐ If you found this project helpful, consider giving it a star!
