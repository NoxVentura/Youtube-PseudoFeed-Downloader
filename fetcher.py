import csv
import subprocess
import time
from datetime import datetime, timedelta
import argparse


def main():
    # start time
    start = time.time()

    # opens the file in a context manager
    with open(SUBSCRIPTIONS_PATH, 'r') as file:
        csvreader = csv.reader(file)
        # skips header
        next(csvreader)
        for row in csvreader:
            # ignores invalid lines
            if not row:
                continue
            # gives the channel playlist
            channel_link = row[1]
            uploads_playlist = f"{channel_link}/videos"
            # calls downloader
            call_downloader(uploads_playlist)

    # end time
    end = time.time()
    time_taken = (end - start)/60
    print(f"The program took {time_taken} minutes to complete")


def check_validity(uploads_playlist, playlist_item):
    checker_command = f'{YT_DOWNLOADER_PATH} {uploads_playlist} -I {playlist_item} --get-filename -o "%(upload_date)s"'.split(" ")
    date_unformatted = subprocess.run(checker_command, capture_output=True, text=True)

    date_formatted = date_unformatted.stdout.strip('\n# ')
    # This shouldn't be a problem but weirdly i'm getting this error
    if date_formatted == '':
        return False
    video_date = datetime.strptime(date_formatted, "%Y%m%d")
    week_ago = datetime.now() - timedelta(days=DAYS_BEFORE)

    return week_ago <= video_date


def call_downloader(uploads_playlist):
    for playlist_item in range(1, VIDEO_COUNT + 1):
        if not check_validity(uploads_playlist, playlist_item):
            continue
        final_command = f"{YT_DOWNLOADER_PATH} --download-archive {LOG_PATH} {uploads_playlist} -I {playlist_item}".split(" ")
        subprocess.run(final_command)


if __name__ == '__main__':
    # argparse initialization
    parser = argparse.ArgumentParser()

    parser.add_argument("--daysbefore", help="daysbefore", nargs='?', type=int, const=7, default=7)
    parser.add_argument("--videocount", help="videocount", nargs='?', type=int, const=1, default=1)

    parser.add_argument("--subscriptionspath", help="subscriptions_path", nargs='?', type=str,
                        const="./subscriptions.csv", default="./subscriptions.csv")
    parser.add_argument("--downloaderpath", help="downloaderpath", nargs='?', type=str, const="./yt.exe",
                        default="./yt.exe")
    parser.add_argument("--logpath", help="logpath", nargs='?', type=str, const="download_log.txt",
                        default="download_log.txt")

    args = parser.parse_args()

    SUBSCRIPTIONS_PATH = args.subscriptionspath
    YT_DOWNLOADER_PATH = args.downloaderpath
    LOG_PATH = args.logpath

    DAYS_BEFORE = args.daysbefore
    VIDEO_COUNT = args.videocount
    
    main()
