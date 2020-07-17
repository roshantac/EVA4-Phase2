# Session 1 - Deploying Mobilenet_v2 model over AWS

## 1. Executive Summary
**Group Members:** *Ramjee Ganti, Srinivasan G, Roshan, Dr. Rajesh and Sujit Ojha* 

### **Objective**:

Deploy a pre-trained PyTorch model - Mobilenet_v2 on AWS Lambda using Serverless and then use it to classify our images. 

### **Results**:

- Hosted the model at this endpoint : https://fyia7867vd.execute-api.ap-south-1.amazonaws.com/dev/classify
- Ran for this image: [Yellow-Labrador-Retriever](data/Yellow-Labrador-Retriever.jpg)
- Response is shown below 
<img src=api_response_insomnia_snapshots.png>


### **Key Highlights**
- Cloud based image classifer at small cost and fast response ~250 ms.
- Keeping function code and it's dependencies less than 250MB (deployment package .zip file) to meet the requirement. Using docker & python installation wheel to manage the contraints.
- Using [Serverless](https://www.serverless.com/) open source framework for building application on AWS Lambda.
- Checked code using pylint to follow docstyle(PEP257) and codestyle(PEP8)



## 2. Steps (Developer Section)
1. Pre-requisites
    - Docker Installation 
        - For mac: https://www.docker.com/products/docker-desktop
    - AWS free tier account https://aws.amazon.com/free/
    - Python Installation, [miniconda](https://docs.conda.io/en/latest/miniconda.html) to keep requirements lightweight
    - Node.js installation https://nodejs.org/en/
    - Install the Serverless framework: *sudo npm install -g serverless*

2. Download a pre-trained MobileNet_v2 model using [download_pretrained_model.py](download_pretrained_model.py)
3. create a Python Lambda function with serverless Framework
    - *serverless create --template aws-python3 --path S1_aws_lambda_mobilenet_v2*
    - creates 'handler.py' and 'serverless.yml'
4. create an S3 bucket, which holds the model
add a Pytorch to the Lambda Environment 
5. install python requirements plugin
    - *serverless plugin install -n serverless-python-requirements*
    - adding [requirements.txt](requirements.txt)
6. write a prediction function to classify an image inside [handler.py](handler.py)
6. configure the serverless framework to set up the API gateway for inference. [serverless.yml](serverless.yml)
7. test our deployment using [Insomnia](https://insomnia.rest/download/)
    - api, POST with multipart/form-data

## 3. References
- Main reference: [EVA4 Phase2 Session1 class](https://theschoolof.ai/)
- Secondary reference: [Blog: Scaling Machine Learning from ZERO to HERO](https://towardsdatascience.com/scaling-machine-learning-from-zero-to-hero-d63796442526)
- Python Style Guide: https://google.github.io/styleguide/pyguide.html