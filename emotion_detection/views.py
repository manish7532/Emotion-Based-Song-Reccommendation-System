from io import BytesIO
import os
from dotenv import load_dotenv
import base64
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import boto3
from user_management.models import UserEmotionData

# Create your views here.

load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET_KEY = os.getenv("ACCESS_SECRET_KEY")

rekognition = boto3.client(
    "rekognition",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    region_name="us-east-1",
)


@csrf_exempt
def capture_image(request):
    if request.method == "POST":
        captured_image_data = request.POST.get("image")
        if captured_image_data:
            # Decode the base64 image data
            image_data = captured_image_data.split(",")[1]  # Remove the data URI prefix
            image = Image.open(BytesIO(base64.b64decode(image_data)))
            # Convert the image to RGB mode if it's in RGBA mode
            if image.mode == "RGBA":
                image = image.convert("RGB")
            # Convert the PIL Image to bytes
            with BytesIO() as image_bytes_io:
                image.save(image_bytes_io, format="JPEG")
                image_bytes = image_bytes_io.getvalue()

            # Use AWS Rekognition to detect faces
            rekognition_response = rekognition.detect_faces(
                Image={"Bytes": image_bytes}, Attributes=["ALL"]
            )

            # Process the Rekognition response as needed
            # For example, extract emotion information from the response
            if rekognition_response.get("FaceDetails", []) != []:
                emotion = [
                    emotion
                    for face in rekognition_response.get("FaceDetails", [])
                    for emotion in face["Emotions"]
                    if emotion["Type"] in ("HAPPY", "CALM", "SAD")
                ]
                emotion = max(emotion, key=lambda x: x["Confidence"])["Type"]
                obj = UserEmotionData(user=request.user, emotion=emotion)
                obj.save()
                return redirect("song_recommendation:home", emotion)
            return render(
            request, "capture_image.html", {"message": "No Face Detected"}
        )
    return render(request, "capture_image.html")


def capture_image_page(request):
    return render(request, "capture_image.html")


# @csrf_exempt
# def capture_image(request):
#     if request.method == 'POST':
#         captured_image_data = request.POST.get('image')
#         if captured_image_data:
#             # Decode the base64 image data
#             image_data = captured_image_data.split(',')[1]  # Remove the data URI prefix
#             image = Image.open(BytesIO(base64.b64decode(image_data)))
#                         # Convert the image to RGB mode if it's in RGBA mode
#             if image.mode == 'RGBA':
#                 image = image.convert('RGB')
#             # Convert the PIL Image to bytes
#             with BytesIO() as image_bytes_io:
#                 image.save(image_bytes_io, format='JPEG')
#                 image_bytes = image_bytes_io.getvalue()

#             # Use AWS Rekognition to detect faces
#             rekognition_response = rekognition.detect_faces(
#                 Image={'Bytes': image_bytes},
#                 Attributes=["ALL"]
#             )
#             print(rekognition_response)

#             # Process the Rekognition response as needed
#             # For example, extract emotion information from the response
#             if rekognition_response.get('FaceDetails', []) != []:
#                 emotion = [
#                     emotion
#                     for face in rekognition_response.get('FaceDetails', [])
#                     for emotion in face["Emotions"]
#                     if emotion["Type"] in ("HAPPY", "CALM", "SAD")
#                     ]
#                 emotion = max(emotion, key=lambda x: x['Confidence'])["Type"]
#                 obj = UserEmotionData(user=request.user, emotion=emotion)
#                 obj.save()
#                 return redirect("song_recommendation:home", emotion)
#         return redirect("emotion_detection:capture_image_page",{'message': 'No Face Detected'})
#     return redirect("emotion_detection:captture_image",{'message': 'Invalid request method'}, status=400)

# def capture_image_page(request):
#     return render(request, 'capture_image.html')
