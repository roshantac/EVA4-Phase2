import matplotlib
import matplotlib.cm
import numpy as np

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



def MissClassifedImage(dataSet, model,device, dispCount,classes):
  dataiter = iter(dataSet)
  import matplotlib.pyplot as plt
  import numpy as np
  #from GradCam import show_map
  import matplotlib.pyplot as plt


  fig, axs = plt.subplots(dispCount,1,figsize=(10,60))
  count =0
  while True:
      if count >= dispCount:
        break
      images, labels = dataiter.next()
      imagex = images
      images, labels = images.to(device), labels.to(device)
      model= model.to(device)
      output = model(images)
      imagex = images
      a, predicted = torch.max(output, 1) 
      if(labels != predicted):
        imagex = imagex.squeeze()  
        imagex = np.transpose(imagex, (1, 2, 0))
        axs[count,0].imshow(imagex)
        # images = images.squeeze()  
        # images =images.cpu()
        # images = np.transpose(images, (1, 2, 0))
        # axs[count,0].imshow(images)
        axs[count,0].set_title("Orig: "+str(classes[labels])+", Pred: "+str(classes[predicted]))
        fig.tight_layout(pad=3.0)
        count = count +1
  plt.show()
