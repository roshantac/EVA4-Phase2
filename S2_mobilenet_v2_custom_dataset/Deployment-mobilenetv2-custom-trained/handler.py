"""Code to download pre-trained pytorch model.

Download the pre-trained model and convert into trace model
"""
try:
    import unzip_requirements
except ImportError:
    pass
import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image

import boto3
import os
import io
import json
import base64
from requests_toolbelt.multipart import decoder
print("Import End...")

# define env bariables if there are not existing
S3_BUCKET = os.environ['S3_BUCKET'] if 'S3_BUCKET' in os.environ \
    else 'tsai-assignment-models-s2'
MODEL_PATH = os.environ['MODEL_PATH'] if 'MODEL_PATH' in os.environ \
    else 'mobilenet_v2_custom_trained_v4.pt'

print('Downloading model...')

s3 = boto3.client('s3')

try:
    if not os.path.isfile(MODEL_PATH):
        obj = s3.get_object(Bucket=S3_BUCKET, Key=MODEL_PATH)
        print("Creating Bytestream")
        bytestream = io.BytesIO(obj['Body'].read())
        print("Loading Model")
        model = torch.jit.load(bytestream)
        print("Model Loaded...")
except Exception as e:
    print(repr(e))
    raise(e)


def transform_image(image_bytes):
    """Transform the image for pre-trained model.

    Transform the image which includes resizing, centercrop and normalize.

    Args:
        image_bytes: Input image in bytes

    Returns:
        Tensor

    Raises:
        Except: An error occurred accessing the bytes.
    """
    try:
        transformations = transforms.Compose([
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        image = Image.open(io.BytesIO(image_bytes))
        return transformations(image).unsqueeze(0)
    except Exception as e:
        print(repr(e))
        raise(e)


def get_prediction(image_bytes):
    """Prediction from pre-trained model.

    Inferecing using pre-trained model

    Args:
        image_bytes: Transformed image_bytes

    Returns:
        int, predicted class index from imagenet
    """
    tensor = transform_image(image_bytes=image_bytes)
    return model(tensor).argmax().item()


def classify_image(event, context):
    """Classify image using api.

    Function is called from this template python: handler.py

    Args:
        event: Dictionary containing API inputs 
        context: Dictionary

    Returns:
        dictionary: API response

    Raises:
        Exception: Returning API repsonse 500
    """
    try:
        content_type_header = event['headers']['content-type']
        # print(event['body'])
        body = base64.b64decode(event["body"])
        print('BODY LOADED')

        picture = decoder.MultipartDecoder(body, content_type_header).parts[0]
        prediction = get_prediction(image_bytes=picture.content)
        print(prediction)

        class_names = ['Large QuadCopters', 'Flying Birds', 'Small QuadCopters', 'Winged Drones']

        prediction_label = class_names[prediction]

        filename = (picture
                    .headers[b'Content-Disposition']
                    .decode().split(';')[1].split('=')[1])

        if len(filename) < 4:
            filename = (picture
                        .headers[b'Content-Disposition']
                        .decode().split(';')[2].split('=')[1])

        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
            "body": json.dumps({'file': filename.replace('"', ''),
                                'predicted': f"{prediction}, {prediction_label}"})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            "body": json.dumps({"error": repr(e)})
        }
