# Task 3 · Image Captioning using Pre-Trained Vision-Language Model

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Model](https://img.shields.io/badge/Model-Salesforce%2Fblip--image--captioning--base-blue?style=for-the-badge)

An end-to-end Deep Learning Image Captioning application built for the **CODSOFT Internship (Task 3)**. It leverages **transfer learning** with Salesforce's pre-trained **BLIP (Bootstrapping Language-Image Pre-training)** vision-language model to automatically interpret visual scenes and generate natural English descriptions.

---

## 📌 Project Overview

Image Captioning sits at the intersection of **Computer Vision** and **Natural Language Processing (NLP)**. Rather than training large Vision-Transformer (ViT) and text-decoder architectures from scratch—which requires tens of thousands of GPU hours—this project demonstrates real-world ML deployment using state-of-the-art pre-trained foundation models.

---

## 🧠 Model Architecture & Pipeline

```text
               ┌───────────────────────┐
               │      Input Image      │
               └───────────┬───────────┘
                           │
                           ▼
          ┌──────────────────────────────────┐
          │  Preprocessing via BlipProcessor │
          │  (Resize, Normalize, Tensorize)  │
          └────────────────┬─────────────────┘
                           │
                           ▼
          ┌──────────────────────────────────┐
          │        BLIP Vision Encoder       │
          │     (Vision Transformer / ViT)   │
          └────────────────┬─────────────────┘
                           │ Visual Feature Embeddings
                           ▼
          ┌──────────────────────────────────┐
          │        BLIP Text Decoder         │
          │    (Autoregressive Generation)   │
          └────────────────┬─────────────────┘
                           │
                           ▼
          ┌──────────────────────────────────┐
          │    Post-Processing & Output      │
          │  "A woman sitting on a bench..." │
          └──────────────────────────────────┘
```

---

## 🚀 Features

- **Dual Interfaces**:
  - 🖥️ **CLI Mode** (`image_captioning.py`): Interactive terminal prompt with automatic history logging.
  - 🌐 **Web Server Mode** (`server.py`): Built-in zero-dependency HTTP server with image upload and instant caption display.
- **Pre-trained SOTA Model**: Uses `Salesforce/blip-image-captioning-base`.
- **Heuristic Post-Processing**: Filters out common grammar and pluralization artifacts.
- **Log Archiving**: Captions automatically saved to `outputs/captions.txt`.

---

## 📁 Directory Structure

```text
Task-3_Image_Captioning/
├── image_captioning.py   # CLI entry point for model inference
├── server.py             # Local Web UI server for uploading and previewing images
├── requirements.txt      # PyTorch, Transformers, Pillow dependencies
├── sample_images/        # Curated test images
│   ├── image1.jpg        # Person in a scene
│   ├── image2.jpg        # Animal / pets
│   └── image3.jpg        # Landscape / object
├── outputs/              # Generated caption logs
│   └── captions.txt
├── docs/                 # Detailed reports & writeups
│   ├── Project_Report.md
│   ├── Project_Report.pdf
│   ├── Final_Task_Report.md
│   └── Final_Task_Report.pdf
└── README.md             # This documentation
```

---

## 💻 Installation & Usage

### 1. Install Dependencies
```bash
cd Task-3_Image_Captioning
pip install -r requirements.txt
```

### 2. Run via Command Line Interface (CLI)
```bash
python image_captioning.py
```
*Prompt: Enter `sample_images/image1.jpg` to run inference on the test image.*

### 3. Run via Local Web Server
```bash
python server.py
```
Open your browser and navigate to `http://localhost:8000`. You can upload any image directly to inspect real-time caption generation!

---

## 📊 Sample Inference Results

| Image | Sample Description | Generated Model Caption |
|---|---|---|
| `sample_images/image1.jpg` | Human subject | *"A woman sitting on a bench in the park."* |
| `sample_images/image2.jpg` | Animal / Pet | *"A dog running through the green grass."* |
| `sample_images/image3.jpg` | Landscape | *"A scenic mountain range under a cloudy sky."* |

---

## 📄 Documentation & Reports
Full formal internship reports are provided inside the [`docs/`](docs/) directory:
- 📑 **[`Project_Report.md`](docs/Project_Report.md)**: Task 3 Machine Learning Model Exploration Report.
- 📑 **[`Final_Task_Report.md`](docs/Final_Task_Report.md)**: AI & ML In The Real World Report.
