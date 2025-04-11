import os

directory = "C:/Users/Deepanshu/handson"
largest = max(
    ((os.path.join(root, file), os.path.getsize(os.path.join(root, file)))
     for root, _, files in os.walk(directory) for file in files),
    key=lambda x: x[1]
)
print(f"Largest file: {largest[0]}\nSize: {largest[1]} bytes")
