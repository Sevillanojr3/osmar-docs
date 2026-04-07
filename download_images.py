"""Download high-quality images from Unsplash for each section."""
import urllib.request
import os

OUT = "/mnt/c/Users/jesus/Workspace-Dev_Projects/osmar-docs/static/images"
os.makedirs(OUT, exist_ok=True)

# Unsplash source URLs (free, no API key needed, high quality)
# Format: https://images.unsplash.com/photo-ID?w=WIDTH&q=QUALITY&fit=crop
images = {
    "hero": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=800&h=800&q=80&fit=crop",
    "problem": "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=800&h=800&q=80&fit=crop",
    "philosophy": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&h=800&q=80&fit=crop",
    "ingredients": "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?w=800&h=800&q=80&fit=crop",
    "sugar": "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=800&h=800&q=80&fit=crop",
    "marketing": "https://images.unsplash.com/photo-1542838132-92c53300491e?w=800&h=800&q=80&fit=crop",
    "macros": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800&h=800&q=80&fit=crop",
    "portions": "https://images.unsplash.com/photo-1547592180-85f173990554?w=800&h=800&q=80&fit=crop",
    "practice": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=800&q=80&fit=crop",
    "closing": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&h=800&q=80&fit=crop",
}

for name, url in images.items():
    filepath = os.path.join(OUT, f"{name}.jpg")
    if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
        print(f"[SKIP] {name}.jpg exists")
        continue
    print(f"[DL] {name}.jpg ...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            with open(filepath, "wb") as f:
                f.write(data)
            print(f"[OK] {name}.jpg ({len(data)//1024}KB)")
    except Exception as e:
        print(f"[ERR] {name}: {e}")

print("\nDone!")
for f in sorted(os.listdir(OUT)):
    fp = os.path.join(OUT, f)
    print(f"  {f} - {os.path.getsize(fp)//1024}KB")
