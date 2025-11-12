import numpy as np
import cv2
from matplotlib import pyplot as plt
import json
import os
# for future note when coming back (use git add, git commit -m "" and then git push)
# find a way to get a input of a picture (encoding, possible options are numpy, tensorflow)

#prompt input for file location
#photo = input("Enter file location: ") to use later if i dont want to have to input image in terminal




#function to run Opencv canny edge detection to get edges
def get_cvedges(image_path):
    #Load image
    image = cv2.imread(image_path)
    # convert to grayscale and new filename is gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detector
    edged_image = cv2.Canny(gray, 100, 200)
    #get contours
    contours, hierarchy = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #extract heigh and width of image inputted
    height, width = edged_image.shape
    desmos_lines = [] #list of strings for all contours
    all_points = [] #list of all contour for json export as tuple

    for contour in contours:
        lines = []
        #simplify contour array output from opencv to fit python array
        for (x, y) in contour[:, 0]:
            x_scaled = (x - width / 2) / (width / 20)   # scale to roughly [-10,10]
            y_scaled = (height / 2 - y) / (height / 20)
            lines.append((x_scaled, y_scaled))
        #join each point  x and y with a comma and space for desmos input
        desmos_points = " , ".join([f"({x:.2f},{y:.2f})" for x, y in lines])
        desmos_lines.append(desmos_points)
        all_points.append(lines)  # Save for JSON export
    return desmos_lines, all_points

image_path = r"C:\Users\User\Pictures\gojo gigachad.jpg"
desmos_strings, desmos_all_contours = get_cvedges(image_path)

# Build Desmos state JSON
desmos_state = {
    "expressions": {
        "list": [
            {
                "type": "expression",
                "id": f"contour{i+1}",
                "latex": "{" + ", ".join(f"({x:.2f},{y:.2f})" for x, y in contour) + "}"
            }
            for i, contour in enumerate(desmos_all_contours)
        ]
    }
}   

#get user path to downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "desmos_state.json")

# Save JSON
with open(file_path, "w") as f:
    json.dump(desmos_state, f, indent=2)

print(f"Desmos JSON file saved to: {file_path}")
    


#check that it is in jpeg/png

#run input through program


# read the information of the picture
# find the main features of the picture (maybe start with face first)
    # use an ai to recognize the main features
# convert the ai to meaningful results ( convert it to graph equations)
    # what kind of graphs?
# find a way to put the graph outputs in desmos automatically
    # ideally itll redirect with a link to a desmos website

