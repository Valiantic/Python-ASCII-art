from PIL import Image

def image_to_text_art(image_path, word):
    try:
        image = Image.open(image_path).convert("L")
        
        width, height = image.size
        aspect_ratio = height / width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.55)  
        image = image.resize((new_width, new_height))
        
        pixels = image.getdata()
        ascii_art = []
        word_length = len(word)
        
        for i, pixel in enumerate(pixels):
            char_index = pixel * word_length // 256  
            ascii_art.append(word[char_index % word_length])  
        
       
        ascii_art = ''.join(ascii_art)
        ascii_lines = [ascii_art[i:i + new_width] for i in range(0, len(ascii_art), new_width)]
        return "\n".join(ascii_lines)
    
    except Exception as e:
        return f"An error occurred: {e} make sure to include file exetension in the path"

if __name__ == "__main__":
    
    while True: 
            
            # word = input("Enter a word to use for the text art: ").strip()
            word = "the quick brown fox jumps over the lazy dog"
            
            
            print(r"""
            ___________              __     _____          __          
            \__    ___/___ ___  ____/  |_  /  _  \________/  |_________
            |    |_/ __ \\  \/  /\   __\/  /_\  \_  __ \   __\___   /
            |    |\  ___/ >    <  |  | /    |    \  | \/|  |  /    / 
            |____| \___  >__/\_ \ |__| \____|__  /__|   |__| /_____ \
                        \/      \/              \/                  \/
            """)

          
            image_path = input("Enter the path to the image file: ").strip()
            
            # Generate text art
            text_art = image_to_text_art(image_path, word)
            
            # Print the result
            print("\nGenerated Text Art:")
            print(text_art)
