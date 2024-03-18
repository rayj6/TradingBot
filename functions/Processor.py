import cv2
from colorama import Fore

def ShowImage(image):
    cv2.imshow(f"Image with Max Similarity Score", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ImageProcessor(image2):
    data = []  # List to hold dictionaries containing ID and link data
    arr = []   # List to hold similarity scores

    for i in range(1, 8):
        image_link = '../data/BTC/uptrend/' + str(i) + '.png'
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
        print(f"Similarity Score for ID {i}: ", round(metric_val, 2))
        arr.append(float(round(metric_val, 2)))

    max_similarity_score = max(arr)
    print("\nMax Similarity Score:", max_similarity_score)

    # Find the ID of the image with the maximum similarity score
    max_similarity_index = arr.index(max_similarity_score)
    print("Image ID with Max Similarity Score:", data[max_similarity_index]["id"])

    if (max_similarity_score >= 0.95):
        print("In this case, you should enter: " + Fore.GREEN + "Long", Fore.RESET)
    else:
        print("In this case, you should enter: " + Fore.RED + "Short", Fore.RESET)

    max_similarity_image = cv2.imread(data[max_similarity_index]["link"])
    print("Your position is similar to this case")
    ShowImage(max_similarity_image)
    


image = cv2.imread('../data/test/test3.png')
ImageProcessor(image)
