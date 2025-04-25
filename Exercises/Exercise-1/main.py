import requests
import os
import zipfile
from pathlib import Path

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_and_extract_file(uri, download_dir):
    try:
        filename = uri.split('/')[-1]
        zip_path = os.path.join(download_dir, filename)
        
        print(f"Downloading {filename}...")
        response = requests.get(uri)
        response.raise_for_status()
        
        with open(zip_path, 'wb') as f:
            f.write(response.content)
            
        print(f"Extracting {filename}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_dir)
            
        os.remove(zip_path)
        print(f"Successfully processed {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {uri}: {str(e)}")
        return False
    except zipfile.BadZipFile:
        print(f"Error: {filename} is not a valid zip file")
        return False
    except Exception as e:
        print(f"Error processing {uri}: {str(e)}")
        return False

def main():
    download_dir = "downloads"
    Path(download_dir).mkdir(exist_ok=True)
    
    successful_downloads = 0
    for uri in download_uris:
        if download_and_extract_file(uri, download_dir):
            successful_downloads += 1
            
    print(f"\nDownload complete. Successfully processed {successful_downloads} out of {len(download_uris)} files.")

if __name__ == "__main__":
    main()
