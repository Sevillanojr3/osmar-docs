"""Generate images for the storytelling website using Gemini API."""
import os
import sys
import time

# Set API key
os.environ["GEMINI_API_KEY"] = "AIzaSyCnZsF_QK-IWgKtaflzz7Wt-35GmoD86AM"

from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

OUTPUT_DIR = "/mnt/c/Users/jesus/Workspace-Dev_Projects/osmar-docs/static/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Image prompts for each section
images = [
    {
        "name": "hero",
        "prompt": "Minimalist flat illustration of a strong person confidently holding a magnifying glass examining a food nutrition label, dark background with subtle green gradient glow, modern SaaS style, clean vector art, soft shadows, fitness and health theme, no text"
    },
    {
        "name": "problem",
        "prompt": "Minimalist flat illustration of a grocery store shelf filled with colorful food packages with misleading marketing labels like stars and badges, dark background, deceptive branding concept, modern SaaS illustration style, soft red warning glow, clean vector art, no text"
    },
    {
        "name": "philosophy",
        "prompt": "Minimalist flat illustration of a balanced plate with 80% fresh whole foods (vegetables, fruits, proteins) and 20% treats (chocolate, cookies), on a dark background with soft green glow, modern clean SaaS style, harmony and balance concept, no text"
    },
    {
        "name": "ingredients",
        "prompt": "Minimalist flat illustration of a magnifying glass zooming into a food ingredients list on a product package, revealing hidden ingredients, dark background with green accent lighting, modern SaaS vector style, clean and educational, no text"
    },
    {
        "name": "sugar",
        "prompt": "Minimalist flat illustration showing multiple sugar cubes with different name tags attached to each (representing hidden names of sugar), dark background with dramatic red glow, alarming but clean design, modern SaaS style, no text"
    },
    {
        "name": "marketing",
        "prompt": "Minimalist flat illustration of a food product package with a glamorous shiny mask being pulled off to reveal a simple plain package underneath, dark background, unmasking deception concept, modern SaaS vector style, green and gold accents, no text"
    },
    {
        "name": "macros",
        "prompt": "Minimalist flat illustration of three interconnected circles representing carbohydrates (green), proteins (blue), and fats (orange), with small food icons inside each circle, dark background, modern SaaS style, clean infographic feel, no text"
    },
    {
        "name": "portions",
        "prompt": "Minimalist flat illustration of five food group bowls arranged in a row - dairy, fruits, starches, proteins, fats - each with a subtle glow in different colors, dark background, modern clean SaaS vector style, portion control concept, no text"
    },
    {
        "name": "practice",
        "prompt": "Minimalist flat illustration of hands holding a nutrition facts label with colored highlights on key areas (serving size, macros), dark background with green glow, educational and empowering feel, modern SaaS vector style, no text"
    },
    {
        "name": "closing",
        "prompt": "Minimalist flat illustration of a person walking confidently through a grocery store aisle with a subtle green aura of knowledge, dark background, empowerment and freedom concept, modern SaaS vector style, serene and motivational, no text"
    }
]

for img_info in images:
    name = img_info["name"]
    filepath = os.path.join(OUTPUT_DIR, f"{name}.png")

    if os.path.exists(filepath):
        print(f"[SKIP] {name}.png already exists")
        continue

    print(f"[GEN] Generating {name}.png ...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[img_info["prompt"]],
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
            ),
        )

        saved = False
        for part in response.parts:
            if part.inline_data:
                image = part.as_image()
                image.save(filepath, format="PNG")
                print(f"[OK]  {name}.png saved!")
                saved = True
                break

        if not saved:
            print(f"[WARN] No image returned for {name}")

    except Exception as e:
        print(f"[ERR] {name}: {e}")

    time.sleep(2)  # Rate limiting

print("\nDone!")
