# 🚧 Pothole Detection using YOLOv8

## 📌 Overview
This project uses YOLOv8 to detect potholes in road images using deep learning.

## 🚀 Features
- Real-time pothole detection
- High accuracy (mAP50 ≈ 78.9%)
- Fast inference (~20ms per image)
- Multiple pothole detection per image

## 🧠 Model Details
- Model: YOLOv8
- Dataset: Roboflow Pothole Dataset
- Precision: 84.5%
- Recall: 66.1%
- mAP50: 78.9%

## 📂 Project Structure
train.py
predict.py
best.pt
requirements.txt

## ⚙️ Installation
```bash
pip install -r requirements.txt
▶️ Run Prediction
python predict.py
📸 Results
<img width="1920" height="1920" alt="image" src="https://github.com/user-attachments/assets/e3d9237a-c693-4f28-97ac-82f6049b343c" />

💡 Future Improvements
Real-time video detection
Severity classification
Web dashboard integration

