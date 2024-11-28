from collections import defaultdict

def parse_string(files_string):
    files = files_string.split(", ")
    files_grouped_by_extension = defaultdict(list)

    for file in files:
        _, extension = file.rsplit(".", 1)
        files_grouped_by_extension[extension].append(file)

    grouped_files_string = []

    for extension, file_group in files_grouped_by_extension.items():
        grouped_files_string.append(", ".join(file_group))

    return "\n".join(grouped_files_string)

files_string = "plik1.jpg, plik2.gif, plik3.mid, plik4.jpg"
print(parse_string(files_string))
