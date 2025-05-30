import numpy as np

def allocate_tensor():
    shape = (8192, 4096)
    try:
        print(f"Allocating tensor with shape {shape}")
        x = np.zeros(shape, dtype=np.float32)
    except MemoryError:
        raise MemoryError(f"Out of memory error when allocating tensor with shape {shape}")

def main():
    allocate_tensor()

if __name__ == "__main__":
    main()
