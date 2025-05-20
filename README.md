# CarPiston Counter

This repository provides a complete solution for detecting and counting car pistons (P1, P2, P3, P4) using a YOLOv8 object detection model. The trained model is integrated into a FastAPI backend to serve real-time predictions through an API.

## Project Structure

- 'CarPiston_API/'  
  FastAPI backend for handling image uploads and returning prediction results.

- 'YOLOv8_Piston_Detection_Model_Training.ipynb'  
  Jupyter notebook used to train and evaluate the YOLOv8 object detection model.

- 'piston detection.v1i.yolov8/'  
  Directory containing the labeled dataset (images, annotations, config files).

## Requirements

Python 3.10 or higher

ultralytics

fastapi

uvicorn

opencv-python

numpy

pillow

python-multipart

## How to Use

### 1. Clone the Repository

'''bash
git clone https://github.com/Aliane-lian/CarPiston_counter.git
cd CarPiston_counter

### 2. Install Dependencies  
Ensure you are using Python 3.10 or later. Then install the required packages:

pip install ultralytics fastapi uvicorn opencv-python pillow numpy python-multipart

### 3. Run the API Sever  
Navigate to the FastAPI backend folder:

cd CarPiston_API
uvicorn main:app --reload

Then open your browser and go to:
http://127.0.0.1:8000/docs

You can upload an image through the Swagger UI to receive detection results showing how many pistons were found (P1, P2, P3, P4).


