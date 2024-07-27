from PIL import Image



def encrypt_image(image_path, shift=50):

    original_image = Image.open("C:/Users/YUG/Documents/certi/Internships/Prodigy Infotech/Task2/form.png")

    encrypted_image = Image.new("RGB", original_image.size)



    for x in range(original_image.width):

        for y in range(original_image.height):

            pixel = original_image.getpixel((x, y))

            if isinstance(pixel, int):

                pixel = (pixel, pixel, pixel)

            r,g, b = pixel

            encrypted_r = (r + shift) % 256

            encrypted_g = (g + shift) % 256

            encrypted_b = (b + shift) % 256

            encrypted_image.putpixel((x, y), (encrypted_r, encrypted_g, encrypted_b))



    encrypted_image.save("encrypted_image.png")

    print("Image encrypted and saved as encrypted_image.png")



def decrypt_image(encrypted_image_path, shift=50):

    encrypted_image = Image.open(encrypted_image_path)

    decrypted_image = Image.new("RGB", encrypted_image.size)



    for x in range(encrypted_image.width):

        for y in range(encrypted_image.height):

            r, g, b = encrypted_image.getpixel((x, y))

            decrypted_r = (r - shift) % 256

            decrypted_g = (g - shift) % 256

            decrypted_b = (b - shift) % 256

            decrypted_image.putpixel((x, y), (decrypted_r, decrypted_g, decrypted_b))



    decrypted_image.save("decrypted_image.png")

    print("Image decrypted and saved as decrypted_image.png")



encrypt_image("C:/Users/YUG/Documents/certi/Internships/Prodigy Infotech/Task2/form.png")

decrypt_image("encrypted_image.png"
