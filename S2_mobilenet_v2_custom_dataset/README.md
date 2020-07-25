# Session 2 - Deploying Mobilenet_v2 model for Custom Dataset


## 1. Executive Summary
**Group Members:** *Ramjee Ganti, Srinivasan G, Roshan, Dr. Rajesh and Sujit Ojha* 

### **Objective**:

- Group challenge involving data curation for different flying objects like bird, drones. Our group target is to curate 1000 image of large quadcopter.
- Train mobilenet_v2 model for custom dataset
- Deploy a the model on AWS Lambda using Serverless and then use it to classify our images. 

### **Results**:



### **Key Highlights**
- Data curation issues - Some of the team didn't followed the requirements.
    - Eg. Flying bird had many issues like, large count of flocking birds, cartoon, non-bird, 
    - Most of the small quadropter are big size then 1 ft.


## 2. Steps (Developer Section)

1. Data Curation
Curated dataset from Kaggle, google, youtube video meeting all the requirements.

2. Data preprocessing & Cleanup
    - Image with size > 448 pixel is resized to 448 pixel, keeping aspect ratio same.
    - Removed ~250 flying bird images as the basic requirements are not met.
    - Curated dataset link: https://drive.google.com/drive/folders/1Xcfk3bJpMkoruQAiY7IJQQkAy0u0CX6u

## 3. References

1. [Image utils developed by Ramjee Gantir](https://github.com/gantir/image_utils/blob/master/utils.py)
