import subprocess
import time
from datetime import datetime, timedelta


def check_validity(uploads_playlist, playlist_item):
    checker_command = f'{YT_DOWNLOADER_PATH} {uploads_playlist} -I {playlist_item} --get-filename -o "%(upload_date)s"'.split(
        " ")
    date_unformatted = subprocess.run(checker_command, capture_output=True, text=True)

    date_formatted = date_unformatted.stdout.strip('\n# ')
    video_date = datetime.strptime(date_formatted, "%Y%m%d")
    week_ago = datetime.now() - timedelta(days=DAYS_BEFORE)

    return week_ago <= video_date


def call_downloader(uploads_playlist):
    for playlist_item in range(1, VIDEO_COUNT + 1):
        if not check_validity(uploads_playlist, playlist_item):
            continue
        final_command = f"{YT_DOWNLOADER_PATH} --download-archive {LOG_PATH} {uploads_playlist} -I {playlist_item}".split(
            " ")
        subprocess.run(final_command)


if __name__ == '__main__':
    start = time.time()
    uploads_playlist = "https://www.youtube.com/@MxRPlays/videos"
    SUBSCRIPTIONS_PATH = "./subscriptions.csv"
    YT_DOWNLOADER_PATH = "./yt.exe"
    LOG_PATH = "download_log.txt"

    DAYS_BEFORE = 7
    VIDEO_COUNT = 3
    call_downloader(uploads_playlist)
    end = time.time()
    print((end-start)/60)