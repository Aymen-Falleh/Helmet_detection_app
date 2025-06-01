# Helmet Detection Project

Welcome to the Helmet Detection Project! This repository contains everything you need to detect helmets in images using a YOLOv8-based deep learning model. Whether you want to train your own model or use the provided pretrained one, this guide will walk you through setup, usage, and running the Streamlit app interface.

---

## Project Structure

├───dataset
│ ├───test
│ │ ├───images
│ │ └───labels
│ ├───train
│ │ ├───images
│ │ └───labels
│ └───valid
│ ├───images
│ └───labels
├───results
├───app.py
├───detect_helmet.py
├───train_helmet_detection_model.ipynb
└───requirements.txt

##### Note: The dataset is provided as a .zip file. After decompressing (unzipping) it, you will obtain the folder structure shown above.


- `dataset/`: Contains your images and labels for training, validation, and testing.
- `results/`: This folder will store your inference results (images with detected helmets).
- `app.py`: Streamlit web application for uploading images and detecting helmets interactively.
- `detect_helmet.py`: Script to run helmet detection on a folder of images and save results.
- `train_helmet_detection_model.ipynb`: Jupyter Notebook to train your own helmet detection model.
- `requirements.txt`: List of Python packages needed for this project.

---

## Requirements

To run this project on your machine, we recommend you have:

- Python 3.8 or above
- A CUDA-enabled GPU (optional but highly recommended for training and fast inference)
- Adequate RAM and disk space

You can install all the required Python dependencies easily with:

```bash
pip install -r requirements.txt
```
If your local machine does not have sufficient computational power (especially no compatible GPU), we strongly recommend running this project in Google Colab, where you can access free GPU resources for training and inference.

Using the Pretrained Model
The best.pt file is the pretrained YOLOv8 model included in this project, trained to detect helmets.

Run Detection on a Folder of Images
You can use the detect_helmet.py script to run inference on all images inside a folder, for example on test images:

Train Your Own Model
If you want to train your own helmet detection model:

Prepare your dataset with images and label files in the dataset/train and dataset/valid folders.

Open the Jupyter notebook train_helmet_detection_model.ipynb.

Follow the step-by-step instructions in the notebook to train the model using YOLOv8.

Streamlit App Interface
Run the app with:

```bash
streamlit run app.py
```
The app allows you to:

Upload one or multiple images.

Run helmet detection on the uploaded images.

View the detection results directly.

Download individual results or download all results as a ZIP file if multiple images were processed.

Notes
Ensure your images are in supported formats like JPG, PNG.

You can change the confidence threshold for detections to tune sensitivity.

Results are saved with bounding boxes around detected helmets for easy visualization.

Contact and Feedback
Feel free to reach out if you need help running the project, want to share feedback, or suggest improvements! Your input is valuable.

Demo
![Helmet Detection Demo](demo.gif)


Thank you for checking out the Helmet Detection Project!