import requests
from pathlib import Path

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # Lỗi
]

def download_file(url, dest_folder="downloads"):
    Path(dest_folder).mkdir(parents=True, exist_ok=True)
    filename = url.split("/")[-1]
    filepath = Path(dest_folder) / filename

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception nếu mã lỗi HTTP

        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Tải thành công: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi khi tải {filename}: {e}")

def main():
    for url in download_uris:
        download_file(url)

if __name__ == "__main__":
    main()
