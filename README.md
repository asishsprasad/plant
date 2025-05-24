# Fruit Adulteration Detection System

A machine learning-based solution to detect formaldehyde adulteration in fruits using ppm (parts per million) measurements and fruit type.

## Features

- 🍎 **Fruit Type Support**: Currently supports Apple and Orange detection
- 📊 **ML Model**: K-Nearest Neighbors (KNN) classifier with 99% claimed accuracy
- 🖥️ **GUI Interface**: User-friendly graphical interface built with Tkinter
- ⚖️ **Data Balancing**: Uses SMOTE technique to handle imbalanced datasets
- 📈 **Preprocessing**: Automated data preprocessing pipeline included

## Requirements

- Python 3.6+
- pandas
- scikit-learn
- imbalanced-learn
- joblib
- numpy
- opencv-python
- Pillow
- tkinter

## Installation

1. Clone the repository:
```bash
git clone [your-repository-link]
cd fruit-adulteration-detection
Install dependencies:

bash:
pip install pandas scikit-learn imbalanced-learn joblib numpy opencv-python Pillow
Usage
GUI Mode:

bash:
python gui.py
Use the dropdown to select fruit type

Enter formaldehyde content in ppm

Click "Predict" to get safety result

Model Training:
bash
python model.py
Trains both SVM and KNN models

Saves models to Project_Saved_Models/

Command Line Prediction:

bash
python predict.py
Follow prompts to enter fruit type (1=Apple, 2=Orange) and ppm value
