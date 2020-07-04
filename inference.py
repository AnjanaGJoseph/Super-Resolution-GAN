import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ISR.models import RRDN
def predict(img):
        lr_img = np.array(img)
        model = RRDN(weights='gans')
        sr_img = model.predict(np.array(lr_img))
        return (Image.fromarray(sr_img))