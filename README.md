# CarPiston Counter

This repository contains a complete solution for detecting and counting car pistons (P1, P2, P3, P4) in images 
using a custom YOLOv8 model and serving predictions through a FastAPI backend.

## Project Structure

- 'CarPiston_API/': FastAPI backend for handling image uploads and serving detection results
- 'YOLOv8_Piston_Detection_Model_Training.ipynb': Jupyter notebook used to train and evaluate the YOLOv8 object detection model
- 'piston detection.v1i.yolov8/': Directory containing the dataset used for training, including images, labels, and configuration files

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Use the training notebook to train or test the YOLOv8 model.
4. Run the FastAPI application to perform inference on images through an API.

## Requirements

- Python 3.10 or higher
- 'ultralytics'
- 'fastapi'
- 'uvicorn'
- Other common Python libraries (e.g., numpy, opencv-python, etc.)

