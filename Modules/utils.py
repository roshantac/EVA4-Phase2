import matplotlib
import matplotlib.cm
import numpy as np
import matplotlib.pyplot as plt
import torch

def DepthNorm(depth, maxDepth=1000.0): 
    return maxDepth / depth

class AverageMeter(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def colorize(value, vmin=10, vmax=1000, cmap='plasma'):
    value = value.cpu().numpy()[0,:,:]

    # normalize
    vmin = value.min() if vmin is None else vmin
    vmax = value.max() if vmax is None else vmax
    if vmin!=vmax:
        value = (value - vmin) / (vmax - vmin) # vmin..vmax
    else:
        # Avoid 0-division
        value = value*0.
    # squeeze last dim if it exists
    #value = value.squeeze(axis=0)

    cmapper = matplotlib.cm.get_cmap(cmap)
    value = cmapper(value,bytes=True) # (nxmx4)

    img = value[:,:,:3]

    return img.transpose((2,0,1))



def ShowMissclassifiedImages(model, dataloaders, class_names, class_id, device,dataType='val', num_images=12,save_as="misclassified.jpg"):
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig, axs = plt.subplots(int(num_images/4),4,figsize=(35,35))
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
                  imagex = imagex/np.amax(imagex)
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
