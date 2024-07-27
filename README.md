# pixelManipulation

# Functionality:

# Encryption:

Reads an input image.
Iterates through each pixel's RGB values.
Shifts each color value by the specified amount (default: 50).
Wraps shifted values around 0-255 for color bounds.
Creates a new image with encrypted pixel values.
Saves the encrypted image as "encrypted_image.png".

# Decryption:

Reads an encrypted image.
Reverses the shifting process for each pixel.
Creates a new image with decrypted pixel values.
Saves the decrypted image as "decrypted_image.png"
