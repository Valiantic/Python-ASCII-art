from PIL import Image

def image_to_text_art(image_path, word):
    try:
        # Open the image and convert it to grayscale
        image = Image.open(image_path).convert("L")
        
        # Resize the image for better text output (smaller dimensions for clarity)
        width, height = image.size
        aspect_ratio = height / width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.55)  # Adjust for font aspect ratio
        image = image.resize((new_width, new_height))
        
        # Convert image pixels to ASCII characters
        pixels = image.getdata()
        ascii_art = []
        word_length = len(word)
        
        for i, pixel in enumerate(pixels):
            char_index = pixel * word_length // 256  # Map pixel brightness to word character
            ascii_art.append(word[char_index % word_length])  # Cycle through the word
        
        # Format the ASCII art into the correct dimensions
        ascii_art = ''.join(ascii_art)
        ascii_lines = [ascii_art[i:i + new_width] for i in range(0, len(ascii_art), new_width)]
        return "\n".join(ascii_lines)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    
    while True: 
            # Ask the user for a word
            word = input("Enter a word to use for the text art: ").strip()
            
            # Ask the user for an image file
            image_path = input("Enter the path to the image file: ").strip()
            
            # Generate text art
            text_art = image_to_text_art(image_path, word)
            
            # Print the result
            print("\nGenerated Text Art:")
            print(text_art)
