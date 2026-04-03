#!/usr/bin/env python3
import os, sys, time, requests

API_KEY = os.environ["SYNC_API_KEY"]
AUDIO = sys.argv[1]
VIDEO = sys.argv[2]
OUTPUT = sys.argv[3]

BASE = "https://api.sync.so/v1"
headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}

# Step A: Submit generation job using public URLs
# Since we have local files we must upload them first
# Use the correct upload endpoint
def upload(path):
    with open(path, "rb") as f:
        r = requests.post(
            f"{BASE}/assets",
            headers={"x-api-key": API_KEY},
            files={"file": (os.path.basename(path), f)}
        )
    print(f"Upload {path}: {r.status_code} {r.text[:200]}")
    r.raise_for_status()
    return r.json()


audio_asset = upload(AUDIO)
video_asset = upload(VIDEO)

print("Audio asset:", audio_asset)
print("Video asset:", video_asset)

# Stop here and paste output so we can see
# the actual asset URL structure before proceeding
