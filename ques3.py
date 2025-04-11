from pathlib import Path

source_directory = Path("C:/Users/Deepanshu/handson")
output_file = Path("C:/Users/Deepanshu/merged_output.txt")

text_files = list(source_directory.rglob("*.txt"))

with output_file.open('w', encoding='utf-8') as outfile:
    for txt_file in text_files:
        try:
            content = txt_file.read_text(encoding='utf-8')
            outfile.write(f"\n--- Contents of {txt_file} ---\n")
            outfile.write(content)
            outfile.write("\n\n") 
        except Exception as e:
            print(f"Could not read {txt_file}: {e}")

print("Merging of .txt files complete.")
