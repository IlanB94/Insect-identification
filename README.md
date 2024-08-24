# Insect-identification
A computer vision project for detecting and identifying harmful insects in agricultural environments using images of sticky traps. The project employs image processing techniques and machine learning (YOLOv5) to accurately identify and differentiate insects from other objects, aiding in informed decision-making for pest control.

## Insect Identification in Trap Images
# Project Overview #
This project, conducted as a final project in the Computer Science department at Sapir Academic College in collaboration with Professor Chen Keisar, focuses on identifying harmful insects in agricultural environments using images of sticky traps. The project is divided into two main teams: the detection team and the classification team. Our team's objective is to identify insects in images of sticky traps and differentiate them from irrelevant objects like debris.

#Motivation#
Insects cause significant damage to agricultural production, leading to economic losses globally. Farmers rely on chemical pesticides, which, while effective in controlling insects, also cause severe environmental and health problems. By accurately identifying the presence of harmful insects, farmers can make informed decisions about when and how much to spray, thereby reducing the negative impacts of pesticide use.

#System Architecture# The system is designed to identify insects on sticky traps using image processing algorithms. The identified insects' coordinates are recorded, allowing researchers to analyze and act upon the data. The system has two levels of user access: researchers, who can upload images and retrieve coordinates, and administrators, who manage user permissions and oversee research data.

#Image Processing Workflow#

*Image Acquisition:* Images are acquired from users, typically in high resolution.
*Preprocessing:* Images are converted to grayscale and subjected to Gaussian blur to reduce noise and enhance object edges.
*Thresholding:* The image is converted to a binary format, where the thresholding process differentiates insects (foreground) from the background.
*Object Detection:* Contours are identified, and insects are marked based on their coordinates.
*Output:* The processed image, along with a CSV file containing insect coordinates, is generated.
*Machine Learning Integration:* To improve detection accuracy, machine learning models are trained using a large dataset of labeled insect images. The images undergo a resizing process to optimize memory usage during training. The YOLOv5 model from Ultralytics is used to train the detection algorithm, which is later deployed to identify insects in new images.

#Technologies Used#

**Python:** Core programming language for developing the algorithms.
**OpenCV:** Library used for image processing tasks.
**YOLOv5:** Machine learning framework used for object detection.
**Anaconda:** Python distribution used for managing packages and environments.
**Make Sense:** Tool used for labeling and preparing the dataset.
**Project Demonstrations:** The repository includes step-by-step illustrations of the image processing stages, from raw image acquisition to the final detection output.

