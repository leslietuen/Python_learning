import matplotlib.image as img
import matplotlib.pyplot as plot
myfile = "pf.jpeg"
myimage = img.imread(myfile)
plot.imshow(myimage)
plot.show()
