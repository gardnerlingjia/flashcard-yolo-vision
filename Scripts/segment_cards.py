import sys
from ultralytics import YOLO
from PIL import Image
import os

# 1️⃣ Load model
model = YOLO("runs/detect/train2/weights/best.pt")

# 2️⃣ Get image path from command line
image_path = sys.argv[1]

# 3️⃣ Run detection
results = model(image_path, conf=0.3)
boxes = results[0].boxes.xyxy.cpu().numpy()

# 4️⃣ Open image
img = Image.open(image_path)

# 5️⃣ Create output folder
output_folder = "segmented_cards"
os.makedirs(output_folder, exist_ok=True)

# 6️⃣ Sort boxes by reading order (top-to-bottom, left-to-right)
# First sort by y (row), then by x (column)
boxes_sorted = sorted(boxes, key=lambda b: (b[1], b[0]))

# 7️⃣ Crop and save
for i, (x1, y1, x2, y2) in enumerate(boxes_sorted):
    crop = img.crop((int(x1), int(y1), int(x2), int(y2)))
    crop.save(os.path.join(output_folder, f"card_{i}.png"))

print(f"Saved {len(boxes_sorted)} cards in reading order.")



