from PIL import Image
import os
import sys

def validate_image_file(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("The specified file does not exist")
    
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    if not image_path.lower().endswith(valid_extensions):
        raise ValueError(f"Unsupported file format. Please use one of: {', '.join(valid_extensions)}")

def image_to_text_art(image_path, word):
    try:
        validate_image_file(image_path)
        
        if not word:
            raise ValueError("Word parameter cannot be empty")

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
    
    except FileNotFoundError as e:
        return f"File Error: {e}"
    except ValueError as e:
        return f"Input Error: {e}"
    except Image.UnidentifiedImageError:
        return "Error: Unable to identify image file. Please ensure it's a valid image."
    except Exception as e:
        return f"Unexpected error: {e}"

if __name__ == "__main__":
    try:
        while True: 
            print(r"""
            ___________              __     _____          __          
            \__    ___/___ ___  ____/  |_  /  _  \________/  |_________
            |    |_/ __ \\  \/  /\   __\/  /_\  \_  __ \   __\___   /
            |    |\  ___/ >    <  |  | /    |    \  | \/|  |  /    / 
            |____| \___  >__/\_ \ |__| \____|__  /__|   |__| /_____ \
                        \/      \/              \/                  \/
            """)
            
            image_path = input("Enter the path to the image file (or 'quit' to exit): ").strip()
            
            if image_path.lower() == 'quit':
                print("Exiting program...")
                sys.exit(0)
                
            word = "the quick brown fox jumps over the lazy dog"
            
            text_art = image_to_text_art(image_path, word)
            print("\nGenerated Text Art:")
            print(text_art)
            
            choice = input("\nWould you like to convert another image? (y/n): ").strip().lower()
            if choice != 'y':
                print("Exiting program...")
                break
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Fatal error: {e}")
