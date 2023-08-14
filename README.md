# Youtube-PseudoFeed-Downloader
This script allows you to download YouTube videos listed in a CSV file for a specified range of weeks. It uses a CSV file containing subscription information and a YouTube downloader tool to accomplish this.

## Prerequisites

Before using this script, ensure that you have the following installed:

- Python (version 3 or above)
- yt-dlp binary(renamed as yt.exe)

## Installation

1. Clone this repository to your local machine or download the script files.
2. Install the required Python packages by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

3. Place the Youtube-dlp executable (`yt.exe`) in the same directory as the script file.

## Usage
Everything that applies to youtube-dlp also applies here.
Additionally,

## Usage

1. Prepare a CSV file containing the subscription information. The CSV file should have the following format:

   ```
   channel_name,channel_link
   Channel 1,https://www.youtube.com/channel1
   Channel 2,https://www.youtube.com/channel2
   ...
   ```

   Note: The first row should be the header and should not contain any subscription data.
   This is the default youtube takeout csv file

3. Place the CSV file in the same directory as the script file and name it `subscriptions.csv`.

4. Ensure that you have the YouTube downloader tool (`yt.exe`) in the same directory as the script file.

5. Open a terminal or command prompt and navigate to the directory where the script file is located.

6. Run the script by executing the following command:

   ```shell
   python fetcher.py
   ```

   The script will read the `subscriptions.csv` file, extract the YouTube channel links, and download the corresponding videos using the YouTube downloader tool.

7. The downloaded videos will be saved in the same directory as the script file.

Note: By default, the script downloads videos from the past week. If you want to change the number of weeks for which you want to download videos, you can modify the `--daysbefore`,`--subscriptionpath`, `--videocount` and other cli commands.

## License

This project is licensed under GNU General Public License 3.0.

## Disclaimer

This script is provided as-is and with no warranties. Use it at your own risk. Make sure to comply with YouTube's terms of service and respect the rights of content creators.

---
