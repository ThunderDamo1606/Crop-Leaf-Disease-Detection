# 🌱 Crop Disease Detection from Leaf Images

An end-to-end deep learning project to detect crop diseases from leaf images using CNN and Transfer Learning.  
This system helps farmers and agricultural professionals identify plant diseases early and take preventive actions.

---

## 📌 Project Overview

This project uses **Convolutional Neural Networks (CNN)** and **Transfer Learning (MobileNet)** to classify crop leaf images into different disease categories.  

A **Flask-based web application** is also developed where users can upload a leaf image and instantly get the predicted disease with confidence score.

---

## 🎯 Objectives

- Automatically detect crop diseases from leaf images  
- Implement CNN model from scratch  
- Apply Transfer Learning for better accuracy  
- Perform detailed model evaluation  
- Deploy the model using Flask web application  

---

## 📂 Dataset

The dataset consists of plant leaf images classified into the following categories:

- Bacteria  
- Fungi  
- Healthy  
- Nematode  
- Pest  
- Phytophthora  
- Virus  

### Data Sources
- Kaggle  
- GitHub (PlantVillage Dataset)  

---

## 🧪 Project Workflow

1. **Exploratory Data Analysis (EDA)**
   - Dataset inspection  
   - Class distribution analysis  
   - Sample image visualization  

2. **Preprocessing**
   - Image resizing to 224×224  
   - Normalization  
   - Data augmentation  

3. **Model Development**
   - Custom CNN model  
   - Transfer Learning using MobileNet  

4. **Training**
   - Adam optimizer  
   - Categorical crossentropy loss  

5. **Evaluation**
   - Accuracy & loss curves  
   - Confusion matrix  
   - Classification report  
   - GradCAM visualization  

6. **Deployment**
   - Flask web application  
   - Image upload & prediction interface  

---

## 🧠 Models Used

### 1️⃣ Custom CNN
- Convolution layers  
- MaxPooling  
- Dropout  
- Fully connected layers  

### 2️⃣ MobileNet (Transfer Learning)
- Pretrained on ImageNet  
- Frozen base layers  
- Custom classification head  

---

## 📊 Results

- CNN achieved baseline performance  
- MobileNet provided **higher accuracy and better generalization**  
- Overfitting reduced using:  
  - Dropout  
  - Data augmentation  

---

## 🛠 Tech Stack

- Python  
- TensorFlow / Keras  
- OpenCV  
- Flask  
- NumPy  
- Matplotlib  
- VS Code  
- Jupyter Notebook  

---

## 🚀 How to Run the Project

### Step 1: Clone the repository  
git clone https://github.com/ThunderDamo1606/Crop-Leaf-Disease-Detection  
cd crop-disease-detection  

### Step 2: Create virtual environment  
python -m venv crop_env  
crop_env\Scripts\activate  

### Step 3: Install dependencies  
pip install -r requirements.txt  

### Step 4: Run Flask app  
python app/app.py  

### Step 5: Open in browser  
http://127.0.0.1:5000/  

---

## 🌐 Web Application Features

- Upload crop leaf image  
- Real-time disease prediction  
- Confidence score display  
- Simple and user-friendly interface  

---

## 📁 Project Structure

crop-disease-detection/  
│  
├── data/  
├── notebooks/  
├── src/  
├── models/  
├── app/  
├── templates/  
├── static/  
├── results/  
├── report/  
├── README.md  
└── requirements.txt  

---

## 📌 Future Enhancements

- Support for multiple crops  
- Cloud deployment (AWS / GCP)  
- Mobile application  
- Real-time camera detection  

---

## 👨‍💻 Author

**Damodar Sadavarte**  
📧 Email: damodarsadavarte2000@gmail.com  
🔗 GitHub: https://github.com/ThunderDamo1606  

**Role:**  
Software Developer | Data Analyst | AI & ML Engineer  

---

## ⭐ Support

If you find this project helpful,  
please consider giving it a ⭐ on GitHub.

Thank you!
