from ultralytics import YOLO
import torch

if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    device = 'mps'
else:
    device = 'cpu'

model = YOLO('best.pt')

model.train(
    data='./path/to/data.yaml',
    epochs=100,
    imgsz=640,
    rect=False,
    batch=-1,
    project='runs/train',
    name='exp',
    exist_ok=True,
    patience=30,
    device=device,
    half=True,
    single_cls=True,
    cos_lr=True,
    augment=False,
)
