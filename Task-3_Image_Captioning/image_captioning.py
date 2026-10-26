import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

def load_model():
    print("Loading pre-trained BLIP model (this may take a moment on the first run)...")
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        return processor, model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

def load_image(image_path):
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: Image path '{image_path}' does not exist.")
            return None
            
        # Open and convert image to RGB
        raw_image = Image.open(image_path).convert('RGB')
        return raw_image
    except Exception as e:
        print(f"Error loading image '{image_path}': {e}")
        return None

def fix_caption_grammar(caption):
    """Applies basic post-processing to fix common model spelling/grammar quirks."""
    corrections = {
        "retrieve pup": "retriever pups",
        "golden retrieve": "golden retriever",
        "a dogs": "dogs",
        "a people": "people",
        "a men": "men",
        "a women": "women",
        "a children": "children"
    }
    for wrong, right in corrections.items():
        caption = caption.replace(wrong, right)
    return caption

def generate_caption(processor, model, image):
    print("Processing image...")
    try:
        # Preprocess the image to be suitable for the model
        inputs = processor(image, return_tensors="pt")
        
        # Generate the caption using the pre-trained model
        out = model.generate(**inputs, max_new_tokens=50)
        
        # Decode the generated output back to text
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        # Post-process caption to fix known quirks
        caption = fix_caption_grammar(caption)
        
        return caption
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

def save_caption(image_path, caption):
    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)
    
    try:
        with open("outputs/captions.txt", "a") as f:
            f.write(f"Image: {image_path}\n")
            f.write(f"Caption: {caption.capitalize()}.\n\n")
        print("Caption saved successfully.")
    except Exception as e:
        print(f"Error saving caption: {e}")

def main():
    print("========================================")
    print("       IMAGE CAPTIONING SYSTEM")
    print("========================================")
    
    # Load model once at the beginning
    processor, model = load_model()
    
    if processor is None or model is None:
        print("Failed to load the BLIP model. Exiting.")
        return

    while True:
        print("\nEnter image path:")
        image_path = input().strip()
        
        if not image_path:
            print("Empty input. Please provide a valid image path.")
        else:
            image = load_image(image_path)
            if image:
                caption = generate_caption(processor, model, image)
                
                if caption:
                    print(f"\nGenerated Caption:\n\"{caption.capitalize()}.\"")
                    save_caption(image_path, caption)
                else:
                    print("Could not generate a caption for this image.")
        
        print("\nGenerate caption for another image? (y/n):")
        choice = input().strip().lower()
        if choice not in ['y', 'yes']:
            print("Exiting cleanly. Goodbye!")
            break

if __name__ == "__main__":
    main()
