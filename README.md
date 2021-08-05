# Steganography
Steganography is the method of hiding data in Images. This project implements Steganography in Python using Stepic module with Pillow Module handling the Images. 

Steganography is a part of Cryptography which is the art of hiding data or sending encoded messages. Steganography in particular is the process of hiding data in Images or other multimedia like Video or Audio formats. Steganography main difference between Steganography and Cryptography is that Cryptography hides data indirectly, that is, by changing the structure of the message using keys and various protocols. In Steganography the data is hidden directly, that is, without altering the structure of the message. 

Steganography alters the pixels of the images by changing the Least Significant Bits of the RGB values. This is an effective way to hide the data as the human eye cannot distinguish the images. This project makes use of this technique to hide the data in the image. 

To run this project, the pre-requisites are Stepic and Pillow Modules in Python. To download them, use the below code:

pip install pillow
pip install stepic

Stepic is a Python Module that is used to encode and decode data to and from Images. Pillow is used to handling Images (opening and saving of Images)

Once the pre-requisites are loaded, unload the zip file and copy the code in the code editor. Make sure all the images are ready and run the program. 

Important Note: Stepic works only for images in PNG format. 
