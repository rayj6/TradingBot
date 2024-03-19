import cv2
from colorama import Fore
import os

def ShowImage(image):
    # print(image)
    cv2.imshow(f"Image with Max Similarity Score", image)
    while True:
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

def get_folder_length(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        return -1  # Return -1 to indicate folder does not exist
    
    # List files in the folder
    files = os.listdir(folder_path)
    
    # Return the number of files
    return len(files)

def SetTPSL (currentPosition, Position) :
    if (Position == "Long"):
        TP = currentPosition + currentPosition * 5/100
        SL = currentPosition + currentPosition * 1/100
        print("You should enter " + Fore.GREEN + Position + Fore.RESET + " at " + Fore.YELLOW, currentPosition, Fore.RESET )
        print("TP: "+Fore.GREEN, TP, Fore.RESET)
        print("SL: "+Fore.RED, SL ,Fore.RESET)
    else:
        TP = currentPosition - currentPosition * 5/100
        SL = currentPosition + currentPosition * 1/100
        print("You should enter " + Fore.RED + Position + Fore.RESET + " at " + Fore.YELLOW, currentPosition, Fore.RESET )
        print("TP: " + Fore.GREEN, TP, Fore.RESET)
        print("SL: " + Fore.RED, SL, Fore.RESET)

def ImageProcessor(image2, value):
    data = []  # List to hold dictionaries containing ID and link data
    arr = []   # List to hold similarity scores
    # ShowImage(image2)
    folder_length = get_folder_length("./data/" + value.upper() + "/uptrend/")

    for i in range(1, folder_length + 1):
        image_link = './data/' + value.upper() +'/uptrend/' + str(i) + '.png'
        image_data = {"id": i, "link": image_link}
        data.append(image_data)
        
        image1 = cv2.imread(image_link)
        hist_img1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
        hist_img1[255, 255, 255] = 0  # ignore all white pixels
        cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        hist_img2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
        hist_img2[255, 255, 255] = 0  # ignore all white pixels
        cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        # Find the metric value
        metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
        # print(f"Similarity Score for ID {i}: ", round(metric_val, 2))
        arr.append(float(round(metric_val, 2)))

    max_similarity_score = max(arr)
    print("\nMax Similarity Score:", max_similarity_score)

    # Find the ID of the image with the maximum similarity score
    max_similarity_index = arr.index(max_similarity_score)
    print("Image ID with Max Similarity Score:", data[max_similarity_index]["id"])

    if (max_similarity_score >= 0.95):
        print("In this case, you should enter: " + Fore.GREEN + "Long", Fore.RESET)
        CurrentPosition = float(input("Enter current position: "))
        SetTPSL(CurrentPosition, "Long")
        # max_similarity_image = cv2.imread(data[max_similarity_index]["link"])
        # print("Your position is similar to this case")
        # ShowImage(max_similarity_image)
    else:
        print("In this case, you should enter: " + Fore.RED + "Short", Fore.RESET)
        CurrentPosition = float(input("Enter current position: "))
        SetTPSL(CurrentPosition, "Short")
        

    
