import matplotlib.image as img
myfile = "pf.jpeg"
myimage = img.imread(myfile)
print(myimage.ndim)
print(myimage.shape)
