from PIL import Image
import os
# WE INDICATE THE PATH WHERE THE IMAGES ARE
downloadsFolder = '/Users/Pau Pons/Downloads/'
# WE ASK IF WE CALL OURSELVES THE MAIN FUNCTION
if __name__ == '__main__':
    # WE ITERATE ALL TYPES OF FILES THAT ARE IN THAT FOLDER AND SAVE IT IN THE FILENAME VARIABLE
    for filename in os.listdir(downloadsFolder):
        # WE SPLIT THE EXTENSION AND THE FILE NAME
        name, extension = os.path.splitext(downloadsFolder + filename)
        # WE CHECK IF THE EXTENSION IS ONE OF THESE
        if extension in ['.jpg', '.jpeg', '.png']:
            # WE OPEN THE IMAGES
            picture = Image.open(downloadsFolder + filename)
            # WE SAVE THE PICTURES IN THE SAME FOLDER, ADDING COMPRESSED_ TO HIS NAME, OPTIMIZING IT IN A QUALITY OF 60
            picture.save(downloadsFolder + 'compressed_' + filename, optimize=True, quality=60)


