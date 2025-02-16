import os
import sys
import pyperclip
#Read Files & Combine Contents 
def read_files(file_paths):
    combined_string = ""
    for file in file_paths:
      if os.path.exists(file) and os.path.isfile(file):
        try:
            with open(file, 'r', encoding='utf-8') as f:file_content = f.read()
            filename = os.path.basename(file)
            combined_string += f"\n{filename}\n``` \n"
            combined_string += file_content
            combined_string += f"\n```\n" 
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
      else:
        print(f"File not found or not a valid file: {filename}")
    return combined_string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file1> <file2> ...")
        sys.exit(1)

    file_paths = sys.argv[1:]
    combined_code = read_files(file_paths)
    
    pyperclip.copy(combined_code)
    print(combined_code)  # Output the formatted code