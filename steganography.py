# This program takes an Image and Secret Message from the user. It encrypts the Secret Message into the Image by altering the Image pixels. 
# The decode function, then decodes the encrypted message and prints the Secret Message


# Importing the necessary Modules
from PIL import Image
from os.path import exists
import stepic


# Function that Encrypts the Image with the Secret Message
def hide_msg():
    # Take the Path of the Image from the User
    img_path = input("Enter the Path of the Image you want to Encrypt (with extension): ") 
    
    # Checks for validity of the Image Path
    if exists(img_path) == False:
        print('File does not Exist!')
        exit
    
    # Opens the Image File
    img_open = Image.open(img_path, 'r')

    # Takes the Secret Message from the User
    msg = input("Enter Message to Encrypt: ")
    
    # Checks for the length of the Message. If no Message is typed, then returns error
    if len(msg) == 0:
        print('Enter a Message!')
        exit
    
    # Converts the message string into Bytes
    msg = bytes(msg, 'utf-8')

    # Encodes the Message into the Image
    encode_img = stepic.encode(img_open, msg)

    # Saves the Encoded Message
    save_img = input("Enter the Path where you want to save Secret Image (with extension): ")
    encode_img.save(save_img, format='png')

    # Checks for Validity of the Encrypted Image File
    if exists(save_img) == True:
        print('Image Saved Successfully!')


# Function to Decrypt the Encrypted Image
def reveal_msg():
    # Takes the Path of the Encrypted Image File
    decode_img = input("Enter Path of the Image you want to Decrypt (with extension): ")

    # Checks for validity of the Encrypted Image File
    if exists(decode_img) == False:
        print('File does not Exist!')
        exit

    # Opens the Encrypted Image FIle
    open_img = Image.open(decode_img, 'r')

    # Decrypts the Ecrypted Message from the Encrypted Image
    img_decode = stepic.decode(open_img)
    
    # Prints the Secret Message
    print('The Secret Message is: ' + img_decode)
 

# Main Funtion
def main():
    print('Welcome to Steganography!\n1. Encode\n2. Decode')
    choice = input('Enter your Choice: ')
    if choice == '1':
        hide_msg()
    elif choice == '2':
        reveal_msg()
    else:
        print('Enter a valid choice!')



# Driver Code
if __name__ == '__main__':
    main()