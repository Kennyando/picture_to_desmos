import numpy as np
import cv2
from matplotlib import pyplot as plt
import potrace
# for future note when coming back (use git add, git commit -m "" and then git push)
# find a way to get a input of a picture (encoding, possible options are numpy, tensorflow)

#prompt input for file location
#photo = input("Enter file location: ") to use later if i dont want to have to input image in terminal




#function to run Opencv canny edge detection to get edges
def get_cvedges(image):
    #Load image
    image = cv2.imread(r"C:\Users\User\Pictures\gojo gigachad.jpg", cv2.IMREAD_GRAYSCALE)
    # convert to grayscale and new filename is gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detector
    edged_image = cv2.Canny(gray, 100, 200)
    return edged_image[::-1]
    
def get_potraceedges(image_data):
    

# Display the original image and the edges
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Edges')
plt.imshow(edges, cmap='gray')
plt.show()
#check that it is in jpeg/png

#run input through program


# read the information of the picture
# find the main features of the picture (maybe start with face first)
    # use an ai to recognize the main features
# convert the ai to meaningful results ( convert it to graph equations)
    # what kind of graphs?
# find a way to put the graph outputs in desmos automatically
    # ideally itll redirect with a link to a desmos website

