import torch

CONFIG = {
    "batch_size": 64,
    "learning_rate": 0.01,
    "epochs": 10,
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "model_path": "checkpoints.pth"
}