import matplotlib
import matplotlib.cm
import numpy as np
import matplotlib.pyplot as plt
import torch


def ShowMissclassifiedImages(model, dataloaders, class_names, class_id, device,dataType='val', num_images=12,save_as="misclassified.jpg"):
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig, axs = plt.subplots(int(num_images/4),4,figsize=(20,20))
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders[dataType]):
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
              
            for j in range(inputs.size()[0]):
                if((preds[j] != labels[j]) and (labels[j] == class_id)):
                  row = int((images_so_far)/4)
                  col = (images_so_far)%4
                  imagex = inputs.cpu().data[j]
                  imagex = np.transpose(imagex, (1, 2, 0))
                  imagex=imagex.numpy()
                  mean = np.array([0.53713346, 0.58979464, 0.62127595])
                  std = np.array([0.27420551, 0.25534403, 0.29759673])
                  imagex = std*imagex  + mean
                  imagex = np.clip(imagex, 0, 1)       
                  axs[row,col].imshow(imagex) 
                  fig.tight_layout(pad=2.0)
                  axs[row,col].set_title('Predicted: {} \n Actual: {}'.format(class_names[preds[j]],class_names[labels[j]]))
                  images_so_far += 1
                  if images_so_far == num_images:
                      model.train(mode=was_training)
                      plt.show()
                      fig.savefig(save_as)
                      return
        model.train(mode=was_training)
