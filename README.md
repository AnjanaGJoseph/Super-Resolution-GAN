# Super-Resolution-GAN
## Introduction 
The web app aims to generate a Super Resolution image of your low resolution image using Generative Adversarial Network. Various techniques are adopted for image upscaling which results in distorted image or reduced visual quality images. Deep Learning provides better solution to get optimized images. Super Resolution Genarative Adversarial Network is one amoung them. 

![alt text](demo.gif)
## GAN
Generative Adversarial Networks, or GANs for short, are an approach to generative modeling using deep learning methods, such as convolutional neural networks. Generative modeling is an unsupervised learning task in machine learning that involves automatically discovering and learning the regularities or patterns in input data in such a way that the model can be used to generate or output new examples that plausibly could have been drawn from the original dataset.GANs will have two different networks Generator and a Discriminator. Generator generates the data, which is cross checked by the discriminator. The loss found is rectifided through backpropagation. SR-GAN downsamples the high resolution images to create Low resolution images for training and Generater generates super resolution images and that is cross checked by the Discriminator.

![alt text](https://miro.medium.com/max/2164/1*CcqEeJAa6cOBP8a713YR-w.png)

The output of the SR_GAN could be compared as follows. To know more about the residual deep network (https://arxiv.org/abs/1809.00219)

![alt text](https://miro.medium.com/max/2068/1*7doTQzPZSn3TYFR8xY2FuA.png)

## Dependencies
* ISR - python module 
* numpy - python module 
* PIL - python module 
* Streamlit - Frontend 

## File structure
* srgan_training - Training RRDN and RDN with a little change in hyper-parameters
* app.py - Frontend using streamlit 
* inference.py - predicion file 
* demo.gif - sample working of the web app

## Run
Install the requirements, then run the app.py file. 

## Reference
* https://github.com/tensorlayer/srgan
* https://github.com/deepak112/Keras-SRGAN
* https://github.com/leftthomas/SRGAN
* https://github.com/idealo/image-super-resolution#pre-trained-networks
