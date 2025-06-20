from ultralytics import YOLO
import torch

if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    device = 'mps'
else:
    device = 'cpu'

model = YOLO('best.pt')

metrics = model.val(
    data='./path/to/data.yaml',
    imgsz=640,
    device=device,
    split='val',
    half=True,
    verbose=False
)

print(metrics.speed)
