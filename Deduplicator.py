import hashlib, os, shutil


def calculate_sha256(file_path):
    with open(file_path, "rb") as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()


new_dir = input("Please input the folder to be processed: ")
deleted_dir = input("Please input the folder to store the deleted files: ")
hash_dict = {}

if not os.path.exists(deleted_dir):
    os.makedirs(deleted_dir)

for file_name in os.listdir(new_dir):
    file_path = os.path.join(new_dir, file_name)
    file_hash = calculate_sha256(file_path)
    if file_hash in hash_dict:
        shutil.move(file_path, os.path.join(deleted_dir, file_name))
    else:
        hash_dict[file_hash] = file_path

for dir_name in os.listdir("."):
    if dir_name in [new_dir, deleted_dir] or not os.path.isdir(dir_name):
        continue
    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)
        file_hash = calculate_sha256(file_path)
        if file_hash in hash_dict:
            shutil.move(hash_dict[file_hash], os.path.join(deleted_dir, os.path.basename(hash_dict[file_hash])))
