import csv
import subprocess


def main():
    subscriptions_path = "./subscriptions.csv"
    no_of_videos = int(input("Enter the number of videos to check: "))
    week_check = int(input("Enter the number of weeks you want to check to: "))
    with open(subscriptions_path, 'r') as file:
        csvreader = csv.reader(file)
        # skips header
        next(csvreader)
        for row in csvreader:
            if not row:
                continue
            channel_link = row[1]
            uploads_playlist = f"{channel_link}/videos"
            call_downloader(uploads_playlist,no_of_videos,week_check)


def call_downloader(uploads_playlist,no_of_videos,week_check):
    yt_downloader_path = './yt.exe'
    log_path = 'download_log.txt'
    final_command = f"{yt_downloader_path} --download-archive {log_path} {uploads_playlist} -I 1:{no_of_videos} --dateafter today-{week_check}weeks".split(" ")
    subprocess.run(final_command)


if __name__ == '__main__':
    main()
