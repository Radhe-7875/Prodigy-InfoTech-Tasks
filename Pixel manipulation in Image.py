from PIL import Image

def encrypt_image(image_path, key, output_path):
    """Encrypt an image using a key."""
    try:
        img = Image.open(image_path)
        pixels = img.load()

        # Encrypt each pixel
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )

        # Save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, key, output_path):
    """Decrypt an image using a key."""
    try:
        img = Image.open(image_path)
        pixels = img.load()

        # Decrypt each pixel
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        # Save the decrypted image
        img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool")
    print("---------------------")

    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    image_path = input("Enter the path to the image file: ").strip()
    key = int(input("Enter the encryption key (integer): ").strip())
    output_path = input("Enter the path to save the output image: ").strip()

    if mode == 'encrypt':
        encrypt_image(image_path, key, output_path)
    elif mode == 'decrypt':
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
