from ultralytics import YOLO
import torch

if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    device = 'mps'
else:
    device = 'cpu'

model = YOLO('best.pt')

results = model.predict(
    source='./path/to/images',
    imgsz=640,
    conf=0.25,
    iou=0.45,
    device=device,
    half=True,
    save=True,
    project='runs/detect',
    name='exp',
    exist_ok=True,
    max_det=100,
    verbose=False
)

for result in results:
    pass
