import os
import subprocess
from urllib.parse import urlparse

LINKS_FILE = "links.txt"
OUTPUT_DIR = "pdfs"

def ensure_output_folder():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def get_filename_from_url(url):
    path = urlparse(url).path
    filename = os.path.basename(path)
    return filename or "downloaded.pdf"

def download_pdfs():
    with open(LINKS_FILE, "r") as file:
        urls = [line.strip() for line in file if line.strip()]

    total = len(urls)
    print(f"Starting download of {total} PDFs...\n")

    for i, url in enumerate(urls, 1):
        filename = get_filename_from_url(url)
        output_path = os.path.join(OUTPUT_DIR, filename)
        
        print(f"[{i}/{total}] Downloading: {filename}")
        result = subprocess.run(["curl", "--silent", "--fail", "--output", output_path, url])
        
        if result.returncode == 0:
            print(f"    ✓ Saved to: {output_path}\n")
        else:
            print(f"    ✗ Failed to download: {url}\n")

if __name__ == "__main__":
    ensure_output_folder()
    download_pdfs()
