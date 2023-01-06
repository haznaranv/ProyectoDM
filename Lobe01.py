import base64
import requests

# Save string of image file path below
img_filepath = "C:\\Users\\Haznaranv\\Desktop\\Emociones\\Sonriendo\\images_5.jpg"

# Create base64 encoded string
with open(img_filepath, "rb") as f:
    image_string = base64.b64encode(f.read()).decode("utf-8")

# Get response from POST request
response = requests.post(
    url="http://localhost:38101/v1/predict/42853612-a8a7-4a22-aeb8-4f456abe2bd7",
    json={"image": image_string},
)
data = response.json()
top_prediction = data["predictions"][0]

print(data)

print("======================================================")

# Print the top predicted label and its confidence
print("predicted label:\t{}\nconfidence:\t\t{}"
      .format(top_prediction["label"], top_prediction["confidence"]))