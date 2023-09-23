import os
import io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

# Set your Google Cloud service account credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service_token.json'

# Initialize the Vision API client
client = vision_v1.ImageAnnotatorClient()

# Define your file paths
FOLDER_PATH = r'/Users/puneetwalia/Desktop/hello'
IMAGE_FILE = 'fateh.JPG'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)
OUTPUT_FILE_PATH = os.path.join(FOLDER_PATH, 'output.txt')

# Read the image file
with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

# Create an Image object
image = vision_v1.types.Image(content=content)

# Perform document text detection
response = client.document_text_detection(image=image)

# Extract the text until 'block' is encountered
docText = response.full_text_annotation.text
index = docText.find('block')
if index != -1:
    docText = docText[:index]

# Print the extracted text (optional)
print(docText)

# Write the text to a text file
with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as output_file:
    output_file.write(docText)

# Print a message indicating where the output file was saved
print(f'Output saved to: {OUTPUT_FILE_PATH}')
