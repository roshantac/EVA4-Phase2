'''Plotting Utility.

Grad-CAM implementation in Pytorch

Reference:
[1] xyz
[2] xyz
'''

import matplotlib.pyplot as plt
import numpy as np
import torch

def visualize_model(model, data, device, save_as="visualize.jpg"):
    dataloaders, class_names = data.dataloaders, data.class_names
    was_training = model.training
    model.eval()
    images_so_far = 0
    figure = plt.figure(figsize=(6, 12))
    num_images=5

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders['val']):
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            for j in range(inputs.size()[0]):
                images_so_far += 1
                ax = figure.add_subplot(1, 5, images_so_far, xticks=[], yticks=[])
                ax.axis('off')
                ax.set_title('predicted:\n{}'.format(class_names[preds[j]]),fontsize=14)
                ax.imshow(inputs.cpu().data[j])

                if images_so_far == num_images:
                    model.train(mode=was_training)
                    figure.savefig(save_as)
                    return
        model.train(mode=was_training)
    figure.tight_layout()  
    plt.show()

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.5404, 0.5918, 0.6219])
    std = np.array([0.2771, 0.2576, 0.2998])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title[:4])
    plt.pause(0.001)  # pause a bit so that plots are updated

def imshow_save(inp, save_as="sample.jpg",title=None):
    
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.5404, 0.5918, 0.6219])
    std = np.array([0.2771, 0.2576, 0.2998])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    figure = plt.figure()
    plt.imshow(inp)
    if title is not None:
        plt.title(title[:4])
    plt.pause(0.001)  # pause a bit so that plots are updated
    figure.savefig(save_as)