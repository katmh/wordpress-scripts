import json
import subprocess
import os

with open("../../../../Downloads/authors.json") as f:
    authors = json.load(f)

with open("../../../../Downloads/ids_names_dict.txt") as f:
    ids_names = eval(f.read())

for author in authors:
    name = author["id"]
    print(f"Trying {name}")

    # check if author has image file listed
    if "avatar" in author:

        # find local image
        path = author["avatar"]
        full_relative_path = "../../../../Downloads/" + path

        # upload image and get ID
        image_id = subprocess.check_output(f"wp media import {full_relative_path} --porcelain", shell=True).decode("utf-8").strip()

        # get user ID
        user_id = ids_names[name]

        # update user's avatar field to be image ID
        os.system(f"wp user meta update {user_id} avatar {image_id}")
        print(f"Updated {name}'s avatar with image {image_id}\n")

    else:
        print(f"Skipping {name} {user_id} due to no Twitter handle\n")