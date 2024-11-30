from collections import defaultdict

def parse_string(files_string):
    if not isinstance(files_string, str):
        raise TypeError("Input must be a string")
    if not files_string.strip():
        raise ValueError("Input string cannot be empty or whitespace only")
    
    files = files_string.split(",")
    files_grouped_by_extension = defaultdict(list)

    for file in files:
        if "." not in file or file.startswith(".") or file.endswith("."):
            raise ValueError(f"Invalid file format: {file}")
        
        _, extension = file.rsplit(".", 1)
        files_grouped_by_extension[extension.strip().lower()].append(file.strip())

    grouped_files_string = []

    for extension, file_group in files_grouped_by_extension.items():
        grouped_files_string.append(", ".join(file_group))

    return "\n".join(grouped_files_string)

# files_string = "plik1.jpg, plik2.gif, plik3.mid, plik4.jpg"
# print(parse_string(files_string))
