import hashlib, os


def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), "rb") as f:
                bytes = f.read()
                readable_hash = hashlib.sha256(bytes).hexdigest().upper()
            index = min([i for i in (file.find("["), file.find(".")) if i != -1], default=-1)
            if index != -1:
                new_filename = readable_hash[:8] + file[index:]
                os.rename(os.path.join(root, file), os.path.join(root, new_filename))


rename_files(input("Please enter the folder to rename files in: "))
