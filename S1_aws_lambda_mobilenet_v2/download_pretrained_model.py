"""Code to download pre-trained pytorch model.

Download the pre-trained model and convert into trace model
"""

import torch

# Define the model
model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2',
                       pretrained=True)
model.eval()
# trace model with a dummy input
traced_model = torch.jit.trace(model, torch.randn(1, 3, 224, 224))
traced_model.save('mobilenet_v2.pt')
