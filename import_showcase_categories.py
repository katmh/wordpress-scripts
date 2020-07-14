import os
import json

with open("../../../../Downloads/wordpress-scripts/org_sites.json") as f:
    org_sites = json.load(f)

with open("../../../../Downloads/wordpress-scripts/sites_names_to_ids.txt") as f:
    names_to_ids = eval(f.read())

for site in org_sites:
    name = site["title"]

    # turn categories into string separated by spaces, quotations around each term
    cats = site["categories"]
    cat_string = " ".join('"{0}"'.format(cat) for cat in cats)

    # find post ID corresponding to website
    post_id = names_to_ids[name]

    # run wp-cli command to add categories
    os.system(f"wp post term set {post_id} category {cat_string}")
    print(f"Categories added to {name} {post_id}: {cat_string}\n")