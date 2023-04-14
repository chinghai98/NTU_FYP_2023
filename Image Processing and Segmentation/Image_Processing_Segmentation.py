import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed

# Read image and convert to grayscale
img = cv2.imread("C:/Users/Tan Ching Hai/Desktop/NTU Studies/NTU FYP/ML_Bacteria_Enumeration/ML_for _custom_grid/Pic_2.jpg")
#img = cv2.imread("C:/Users/Tan Ching Hai/Desktop/NTU Studies/NTU FYP/ML_Bacteria_Enumeration/ML_for _custom_grid/Left_pic.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold image
thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]  

# Find contours of objects in binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours to only keep smaller squares
min_area = 80 # 300 for Left_pic
max_area = 300 # 5000 for Left_pic
max_aspect_ratio = 1.3 # -> 2.5 for Left_pic
grids = []
coords = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > min_area and area < max_area:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        if aspect_ratio <= max_aspect_ratio:
            grids.append(cnt)


# Draw bounding rectangles around smaller squares
for cnt in grids:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    coords.append((x,y, x+w,y+h))

# Display result
# cv2.imshow('Result', img)
print(coords)
print(f"No. of grids: {len(coords)}")


'''Count the no. of bacterial colonies in each grid'''
# Count the number of colonies in each grid
for i, grid in enumerate(grids):
    x1, y1, x2, y2 = coords[i]
    grid_img = gray[y:y+h, x:x+w]
    # Threshold grid image
    grid_thresh = cv2.threshold(grid_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # Apply distance transform to get markers for watershed algorithm
    distance = cv2.distanceTransform(grid_thresh, cv2.DIST_L2, 3)
    local_maxi = peak_local_max(distance, min_distance=3, exclude_border=True)
    markers = np.zeros(distance.shape, dtype=np.uint)
    markers[local_maxi[:, 0], local_maxi[:, 1]] = 255
    markers[np.logical_not(grid_thresh)] = 0
    # Apply watershed algorithm
    labels = watershed(-distance, markers, mask=grid_thresh)
    
    # Count bacterial colonies in grid
    colony_count = len(np.unique(labels)) - 1

    # Find center of the grid
    center_x = int((x1+x2)/2)
    center_y = int((y1+y2)/2)
    
    # Draw colony count on original image
    cv2.putText(img, str(colony_count), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)
    # cv2.imwrite('f: crop_{i}.jpg',grid_img)

cv2.imshow('Num',img)

'''# Save cropped image if there are bacteria colonies
if num_colonies > 0:
    cv2.imwrite(f'crop_{i}.jpg', crop)'''



cv2.waitKey(0)
cv2.destroyAllWindows()