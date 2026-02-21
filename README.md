# Flashcard YOLO + Vision LLM Pipeline

Small end-to-end computer vision project:

- Object detection with YOLO (Ultralytics)
- Flashcard segmentation from images
- (Planned) structured content extraction with Google Gemini Vision

---

## 📌 Problem

I have physical flashcards for learning.  
Manually cropping and digitizing them is slow and repetitive.

Goal:
- Automatically detect each flashcard from a photo
- Segment individual cards
- Later: extract structured text (question/answer) using a Vision LLM

---

## 🧠 Pipeline Overview

1. Data labeling with labelImg
2. YOLOv8 training (single class: flashcard)
3. Detection & bounding box extraction
4. Cropping into individual card images
5. (Next step) Gemini Vision for structured text extraction

---

## 📂 Project Structure
# Flashcard YOLO + Vision LLM Pipeline

Small end-to-end computer vision project:

- Object detection with YOLO (Ultralytics)
- Flashcard segmentation from images
- (Planned) structured content extraction with Google Gemini Vision

---

## 📌 Problem

I have physical flashcards for learning.  
Manually cropping and digitizing them is slow and repetitive.

Goal:
- Automatically detect each flashcard from a photo
- Segment individual cards
- Later: extract structured text (question/answer) using a Vision LLM

---

## 🧠 Pipeline Overview

1. Data labeling with labelImg
2. YOLOv8 training (single class: flashcard)
3. Detection & bounding box extraction
4. Cropping into individual card images
5. (Next step) Gemini Vision for structured text extraction

---

## 📂 Project Structure
```text
flashcard-yolo-vision/
├── config/               # YOLO config (e.g. flashcards.yaml)
├── data/                 # dataset placeholder (not in repo)
├── examples/             # example input/output images
├── Scripts/              # project scripts (e.g. segment_page.py)
├── README.md
└── requirements.txt

---

## 💡 What I Learned in This Project

This project helped me move beyond simply training a model and towards building a small, structured AI system.

Key learnings:

- **End-to-end object detection workflow**  
  From dataset structuring and labeling to training, validation, and inference using YOLOv8.

- **Reproducible ML setup**  
  Organizing configuration files, scripts, and dependencies in a clean project structure suitable for version control.

- **Bridging classical CV and LLMs**  
  Designing a pipeline where object detection (YOLO) prepares structured visual inputs for a multimodal LLM (Gemini Vision).

- **Thinking in pipelines, not scripts**  
  Instead of treating models as isolated components, I approached the task as a modular system:
  detection → segmentation → structured extraction → future automation.

This project is a step toward building more advanced AI systems that combine perception (vision models) with reasoning (LLMs).