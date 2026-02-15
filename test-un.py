from unstructured.partition.auto import partition
import torch

print(f"PyTorch Version: {torch.__version__}")
print("PyTorch CUDA Available:", torch.cuda.is_available())

try:
    # Create a dummy file to test
    with open("test.txt", "w") as f:
        f.write("This is a test document for unstructured.")

    elements = partition("test.txt")
    print("\n✅ Unstructured successfully partitioned the file!")
    print(f"Found {len(elements)} elements.")
    print(f"Content: {elements[0].text}")

except Exception as e:
    print(f"\n❌ Error: {e}")