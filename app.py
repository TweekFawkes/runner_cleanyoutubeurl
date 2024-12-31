import sys
from datetime import datetime
import os
from urllib.parse import urlparse, parse_qs

# [*] Default Environment Variables:
# PWD=/tmp/msmowz/20241121173033774104/001
# OLDPWD=/var/task
# LC_CTYPE=C.UTF-8

# [*] Creator Defined Environment Variables:
# SOMETHING=value

def extract_video_id(url):
    # Add https:// prefix if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Handle different YouTube URL formats
    parsed_url = urlparse(url)
    
    # Handle youtu.be URLs
    if parsed_url.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed_url.path[1:]
    
    # Handle youtube.com URLs
    if parsed_url.hostname in ('youtube.com', 'www.youtube.com'):
        # Handle embed URLs
        if parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        # Handle regular URLs with v parameter
        if 'v' in parse_qs(parsed_url.query):
            return parse_qs(parsed_url.query)['v'][0]
    
    return None

def main():
    # Check if URL is provided
    if len(sys.argv) != 2:
        print("[*] Error: Please provide a YouTube URL as an argument")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    video_id = extract_video_id(youtube_url)
    
    if video_id:
        print(f"[*] Shortened URL: youtu.be/{video_id}")
    else:
        print("[*] Error: Invalid YouTube URL provided")
    
if __name__ == "__main__":
    main()
