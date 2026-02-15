from unstructured.partition.auto import partition

# This will test if libmagic, poppler, and tesseract are communicating
try:
    # Use any small pdf or file you have
    elements = partition(filename="example.pdf") 
    print("Success! All dependencies are correctly configured.")
except Exception as e:
    print(f"Setup Error: {e}")