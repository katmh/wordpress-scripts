import json
import subprocess
import os

with open("../../../../Downloads/screenshots.json") as f:
    result = json.load(f)
    sites = result["data"]["allSitesYaml"]["edges"]

with open("../../../../Downloads/ids_sites_dict.txt") as f:
    ids_urls = eval(f.read())

for site in sites:
    url = site["node"]["main_url"]
    print(f"Trying {url}")

    site_id = ids_urls[url]

    # check if site has screenshot
    if site["node"]["childScreenshot"] != "null":
        # get image path
        path = site["node"]["childScreenshot"]["screenshotFile"]["publicURL"]
        image_url = "https://gatsbyjs.org" + path

        # upload image and get ID
        image_id = subprocess.check_output(f"wp media import {image_url} --porcelain", shell=True).decode("utf-8").strip()

        # update site's featured image field to be image ID
        os.system(f"wp post meta update {site_id} screenshot {image_id}")
        print(f"Updated {url}'s screenshot with image {image_id}\n")

    else:
        print(f"Skipping {url} {site_id} due to no screenshot\n")