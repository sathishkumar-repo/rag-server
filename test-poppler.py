import subprocess

try:
    # Test pdfinfo command
    result = subprocess.run(
        ['pdfinfo', '-v'],
        capture_output=True,
        text=True
    )
    print("✅ Poppler is accessible from Python!")
    print(f"Version info: {result.stdout}")
except FileNotFoundError:
    print("❌ Poppler still not found. PATH not updated correctly.")
except Exception as e:
    print(f"⚠️ Error: {e}")