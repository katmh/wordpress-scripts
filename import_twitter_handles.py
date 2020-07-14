import json
import os

with open("../../../../Downloads/authors.json") as f:
    authors = json.load(f)

with open("../../../../Downloads/ids_names_dict.txt") as f:
    ids_names = eval(f.read())

for author in authors:
    name = author["id"]
    print(f"Trying {name}")

    if "twitter" in author:
        user_id = ids_names[name]
        twitter = author["twitter"]
        os.system(f"wp user meta update {user_id} twitter {twitter}")
        print(f"Updated {name} {user_id} with Twitter handle {twitter}\n")

    else:
        print(f"Skipping {name} {user_id} due to no Twitter handle\n")