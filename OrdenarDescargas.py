from PIL import Image
import os

downloadsFolder = "C:/Users/sergi/Downloads/"
picturesFolder = "C:/Users/sergi/Pictures/"


if __name__ == "__main__":

    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".stl"]:
            DocumentoSTL="/Users/sergi/Documents/STL/"
            os.rename(downloadsFolder + filename, DocumentoSTL + filename)
        
        if extension in [".pdf"]:
            DocumentoPDF="/Users/sergi/Documents/"
            os.rename(downloadsFolder + filename, DocumentoPDF + filename)
       

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/sergi/Musica/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
