from PIL import Image
import rembg
import time
import os

def remove_background(image_path):
    # Abrir la imagen con Pillow
    img = Image.open(image_path)
    
    # Eliminar el fondo con rembg
    img_with_alpha = rembg.remove(img)
    
    # Convertir la imagen al modo RGBA
    img_with_alpha = img_with_alpha.convert("RGB")
    
    return img_with_alpha

# Directorio que contiene las imágenes que deseas procesar
input_directory = r"C:\Users\ruben\Downloads\Class_1_25-02\\"

# Directorio donde guardarás las imágenes procesadas
output_directory = r"C:\Users\ruben\Downloads\Class_1_25-02\output_images\\"

# Crear el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Procesar cada imagen en el directorio de entrada y guardar el resultado en el directorio de salida
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        
        # Eliminar el fondo y guardar la imagen resultante
        result_img = remove_background(input_path)
        result_img.save(output_path)

        print(f"Background removed from {filename} and saved as {output_path}")
        time.sleep(3)
