import torch
import matplotlib.pyplot as plt

def show_tensor_image(img: torch.Tensor):
    plt.imshow(img.squeeze().permute(1,2,0))