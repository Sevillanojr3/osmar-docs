"""Generate images trying multiple Gemini models."""
import os, sys, time
os.environ["GEMINI_API_KEY"] = "AIzaSyCnZsF_QK-IWgKtaflzz7Wt-35GmoD86AM"

from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
OUT = "/mnt/c/Users/jesus/Workspace-Dev_Projects/osmar-docs/static/images"
os.makedirs(OUT, exist_ok=True)

# Try these models in order
MODELS = [
    "gemini-2.0-flash",
    "gemini-2.5-flash",
    "gemini-3-pro-image-preview",
    "gemini-2.5-flash-image",
    "gemini-3.1-flash-image-preview",
]

images = [
    ("hero", "Minimalist flat vector illustration, dark background #0a0a0a. A strong confident person holding a large magnifying glass examining a nutrition label. Green accent color #4CAF50. Modern SaaS startup style, soft glow, clean lines, no text, 16:9 wide"),
    ("problem", "Minimalist flat vector illustration, dark background #0a0a0a. A grocery store shelf with colorful deceptive food packages with fake health badges and warning signs. Red accent glow. Modern SaaS style, clean, no text, 16:9 wide"),
    ("philosophy", "Minimalist flat vector illustration, dark background #0a0a0a. A perfectly balanced plate: 80% fresh colorful whole foods on one side, 20% treats on the other. Green #4CAF50 and orange accents. Harmony concept. Modern SaaS style, no text, 16:9 wide"),
    ("ingredients", "Minimalist flat vector illustration, dark background #0a0a0a. A magnifying glass over a food ingredients list revealing hidden text. Green accent #4CAF50, educational feel. Modern SaaS style, clean, no text, 16:9 wide"),
    ("sugar", "Minimalist flat vector illustration, dark background #0a0a0a. Multiple sugar cubes scattered with different name tags like glucosa, fructosa, agave, panela. Red dramatic glow. Alarming but clean design, no text, 16:9 wide"),
    ("marketing", "Minimalist flat vector illustration, dark background #0a0a0a. A glamorous food package mask being pulled off revealing a simple plain product underneath. Green and gold accents. Deception unmasking concept, no text, 16:9 wide"),
    ("macros", "Minimalist flat vector illustration, dark background #0a0a0a. Three large overlapping translucent circles: green for carbs, blue for protein, orange for fat, with small food icons. Infographic style, no text, 16:9 wide"),
    ("portions", "Minimalist flat vector illustration, dark background #0a0a0a. Five elegant bowls in a row representing dairy, fruits, starches, proteins, fats - each glowing a different soft color. Portion control, no text, 16:9 wide"),
    ("practice", "Minimalist flat vector illustration, dark background #0a0a0a. Two hands holding up a nutrition facts label with colorful highlighted key areas like serving size and macros. Empowering feel, green glow, no text, 16:9 wide"),
    ("closing", "Minimalist flat vector illustration, dark background #0a0a0a. A person walking confidently through a grocery store aisle radiating a soft green aura of knowledge. Freedom and empowerment, no text, 16:9 wide"),
]

# First, find a working model
working_model = None
for model in MODELS:
    print(f"[TEST] Trying model: {model}")
    try:
        response = client.models.generate_content(
            model=model,
            contents=["Generate a simple green circle on dark background, minimalist"],
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
            ),
        )
        for part in response.parts:
            if part.inline_data:
                working_model = model
                print(f"[OK] Model {model} works for image generation!")
                break
        if working_model:
            break
        else:
            print(f"[SKIP] {model} returned text only, no image")
    except Exception as e:
        err = str(e)[:100]
        print(f"[ERR] {model}: {err}")
    time.sleep(2)

if not working_model:
    print("\n[FAIL] No model available for image generation. Trying Imagen API...")
    # Try Imagen API
    try:
        from google.genai import types as t
        response = client.models.generate_images(
            model="imagen-4.0-fast-generate-001",
            prompt="A simple green circle on a dark background, minimalist vector art",
            config=t.GenerateImagesConfig(number_of_images=1)
        )
        if response.generated_images:
            working_model = "imagen-4.0-fast-generate-001"
            print(f"[OK] Imagen API works!")
    except Exception as e:
        print(f"[ERR] Imagen: {str(e)[:120]}")

if not working_model:
    print("\n[FATAL] No working image model found. Exiting.")
    sys.exit(1)

print(f"\n=== Using model: {working_model} ===\n")

# Generate all images
for name, prompt in images:
    filepath = os.path.join(OUT, f"{name}.png")
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        print(f"[SKIP] {name}.png exists")
        continue

    print(f"[GEN] {name}.png ...")
    try:
        if "imagen" in working_model:
            from google.genai import types as t
            resp = client.models.generate_images(
                model=working_model,
                prompt=prompt,
                config=t.GenerateImagesConfig(number_of_images=1)
            )
            if resp.generated_images:
                img = resp.generated_images[0].image
                img.save(filepath, format="PNG")
                print(f"[OK] {name}.png saved ({os.path.getsize(filepath)} bytes)")
            else:
                print(f"[WARN] No image for {name}")
        else:
            resp = client.models.generate_content(
                model=working_model,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                ),
            )
            saved = False
            for part in resp.parts:
                if part.inline_data:
                    img = part.as_image()
                    img.save(filepath, format="PNG")
                    print(f"[OK] {name}.png saved ({os.path.getsize(filepath)} bytes)")
                    saved = True
                    break
            if not saved:
                print(f"[WARN] No image for {name}")
    except Exception as e:
        print(f"[ERR] {name}: {str(e)[:120]}")

    time.sleep(3)

print("\nDone! Generated images:")
for f in os.listdir(OUT):
    fp = os.path.join(OUT, f)
    print(f"  {f} ({os.path.getsize(fp)} bytes)")
