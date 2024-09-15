import cv2
import matplotlib.pyplot as plt
def split_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return
    height, width, _ = image.shape
    top_left = image[0:height//2, 0:width//2]
    top_right = image[0:height//2, width//2:width]
    bottom_left = image[height//2:height, 0:width//2]
    bottom_right = image[height//2:height, width//2:width]
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Image Quadrants')
    axs[0, 0].imshow(cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Top Left Quadrant')
    
    axs[0, 1].imshow(cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('Top Right Quadrant')
    
    axs[1, 0].imshow(cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB))
    axs[1, 0].set_title('Bottom Left Quadrant')
    
    axs[1, 1].imshow(cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB))
    axs[1, 1].set_title('Bottom Right Quadrant')
    for ax in axs.flat:
        ax.axis('off')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    image_path = './VK.jpeg'  # Replace with the path to your image file
    split_image(image_path)
