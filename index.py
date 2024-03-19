import cv2
from colorama import Fore

from functions import Processor

def main():
    value = input("Enter value: ")
    image = cv2.imread('./data/test/test22.png')
    Processor.ImageProcessor(image, value)

if __name__ == "__main__":
    print("\n\n")
    print(Fore.YELLOW + "ALERT: This tool is not 100% accurate, please analyze before use" + Fore.RESET)
    main()
    print("\n\n")



    