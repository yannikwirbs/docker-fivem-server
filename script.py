import requests
from bs4 import BeautifulSoup
import os
import sys


# URL of the FiveM build artifacts page
url = "https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/"

# Check if the server is already set up
if os.path.exists("run.sh"):
    print("Server is already set up. Skipping download and extraction.")
else:
    print("Setting up server for the first time...")

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the artifacts page.")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the latest build link
    latest_build = soup.find_all('a', href=True)[3]  # Adjust index if needed
    latest_build_url = url + latest_build.get('href')
    version = list(latest_build.stripped_strings)[0]
    
    print(f"Downloading latest build ({version}) from: {latest_build_url}")

    # Download the tar file
    os.system(f"wget -nv -O fx.tar.xz {latest_build_url}")

    if not os.path.exists("fx.tar.xz"):
        print("Failed to download fx.tar.xz.")
        sys.exit(1)

    # Extract the tar file
    os.system("tar -xf fx.tar.xz")

    # Clean up the tar file
    os.system("rm fx.tar.xz")

# Run the server
os.system("./run.sh")
