# Session 2 - Deploying Mobilenet_v2 model for Custom Dataset


## 1. Executive Summary
**Group Members:** *Ramjee Ganti, Srinivasan G, Roshan, Dr. Rajesh and Sujit Ojha* 

### **Objectives**:

- Group challenge involving data curation for different flying objects like bird, drones. Our group target is to curate 1000 images of large quadcopter.
- Train mobilenet_v2 model for custom dataset
- Deploy the model on AWS Lambda using Serverless and then use it to classify our images. 

### **Results**:



### **Key Highlights**
- Data curation issues 
    - Some of the teams didn't followed the requirements.
    - Eg. Flying birds had many issues like, large count of flocking birds, cartoon, non-bird 
    - Most of the small quadropter are big size then 1 ft.


## 2. Steps (Developer Section)

1. Data Curation:
     - Curated dataset from Kaggle, google, youtube video meeting all the requirements.

2. Data preprocessing & Cleanup:
    - Image with size > 448 pixel is resized to 448 pixel, keeping aspect ratio same.
    - Images converted to *.jpg
    - Removed the .ipynb and txt
    - Removed ~300 flying bird images as the basic requirements are not met.
    - Renamed the files into consistent naming convention and mapping file for classes.
    - Curated dataset link: https://drive.google.com/drive/folders/1Xcfk3bJpMkoruQAiY7IJQQkAy0u0CX6u

3a. Data Structure:    

After clean-up, the images collected where placed in to 4 folders    
    - Flying Birds
    - Large Quadcopters
    - Small Quadcopters
    - Winged Drones
    - All images are zipped in to  https://github.com/EVA4-RS-Group/Phase2/releases/download/s2/final_images_ver2.zip

3b. Data files:    

Data processing also creates 2 files programatically using code present in test_train_csvGen.py
- **datset.csv**  - contains list of images and the corresponding class name. 
- **img_class.csv** - contains list of all images and their respective classes

4. Calculate mean and standard deviation for the dataset:
    - Calculated mean and standard deviation across all images. 
    - This gets used in data tranforms
     
5. Create DroneDataSet at [data_loader.py]https://github.com/EVA4-RS-Group/Phase2/blob/master/Modules/data_loader.py

   DroneSet class that inherits from torch.utils.data.Dataset and perform following
    - Takes as input : train parameter, class names and transforms
    - Load image data based on value of boolean flag train , train data or test data
    - Load Class names
    - Perform transforms on images data 
    - Visualize images

6. Prepare data for training and testing:
    - Split image data as  train data and test data
    - Store images respectively in trainData.csv and testData.csv
    - Based on input parameter passed to DroneSet, the corresponding data gets loads

7. Load **mobilenet_v2** model and determine lr hyper parameter that is passed as input to optimizer and scheduler used in training:
    - Load  model with **pertained option = true**
    - Set value of model parameters **requires_grad = False**
    - Reconstruct final fully connected layer. 
    -   - Parameters of **newly constructed modules have requires_grad=True by default**
    - Pass model to LRFinder(torch-lr-finder)
    - Plot LR values reported by LRFinder
    - Run range_test to determine lr value  using  train dataset

8. Setup Optimizer as **SGD optimiser** and Scheduler as **OneCycleLR**
    - only parameters of final layer are being optimized 
    - Decay LR by a factor of 0.1 every 7 epochs

9. Train using train_model function present in [train.py](https://github.com/EVA4-RS-Group/Phase2/blob/master/Modules/train.py) for 25 epochs:
    - Returns model, loss and accuracy
    - Plot Loss and Accuracy for the train model
    - Visualize images
    
10. Load **mobilenet_v2** model:
    - Set value of model parameters **requires_grad = False**
    - Pass model to LRFinder(torch-lr-finder)
    - Plot LR values reported by LRFinder
    - Run range_test to determine lr value  using  train dataset

11. Train using train_model function present in [train.py](https://github.com/EVA4-RS-Group/Phase2/blob/master/Modules/train.py) for 25 epochs
    - Returns model, loss and accuracy
    - Plot Loss and Accuracy for the train model
    - Visualize images

12. Find and Display misclassified images

13. Save model
    - Save model
    - Please confirm the saved model can be loaded and evaludated again.

## 3. References

1. [Image utils developed by Ramjee Gantir](https://github.com/gantir/image_utils/blob/master/utils.py)
