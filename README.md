CCTV Analytics – AI Powered Video Processing

This project demonstrates a practical use of Artificial Intelligence for real-time video analytics.
It combines YOLOv8 (You Only Look Once, version 8) with OpenCV to detect and analyze objects through a webcam or CCTV feed.

The program opens the camera, performs detection, and overlays results directly on the video stream. The detections are also processed for logging purposes, making it useful for security and surveillance applications.

Features

Real-time object detection using YOLOv8.

Webcam or CCTV input support.

Simple, extendable Python codebase.

Designed as a base for future projects such as:

Automatic License Plate Recognition (ANPR).

Behavior and motion analysis.

Smart alerts for restricted zones.

Tools and Libraries Used

Python 3.10

YOLOv8 (Ultralytics)

OpenCV

Pandas

Streamlit (for dashboards)

Installation Instructions

Clone the repository to your computer.

Create and activate a Python virtual environment.

Install dependencies:

pip install ultralytics

pip install opencv-python

pip install pandas

pip install streamlit

Run the program using:

python main.py

Project Vision

This project is the starting point of building AI-enabled surveillance tools. The current version focuses on real-time object detection, and the roadmap includes:

Recording detections to a database.

Improving video saving compatibility (MP4/H.264).

Creating a web dashboard to monitor multiple cameras.

Author

Developed by Mahad Ahmed
Sydney, Australia
