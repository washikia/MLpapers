import torch

CONFIG = {
    "batch_size": 64,
    "learning_rate": 0.01,
    "epochs": 20,
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "model_path": "checkpoints.pth",
    "train_data_path": './dataset/mnist_train.csv',
    "test_data_path": './dataset/mnist_test.csv',
}