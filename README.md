<p align="center">
  <img src="https://github.com/wrawler/Ani2MAL/blob/main/logo/Ani2mal.png" alt="Description" width="300">
</p>

Ani2MALis a tool that allows you to export your anime list from your streaming sites to [MyAnimeList](https://myanimelist.net).

# Getting Started 🚀

## Supported Websites for export data
Exported Anime watchlist from these websites are only compatible for this script.

- [aniwatchtv.to](https://aniwatchtv.to)
- [hianime.to](https://hianime.to)

If you use any other website, you might have to see workarounds to import those export files into above listed websites and download the export files from them .

I might add support for other websites in near future 😄.

## Prerequisites ✅

- Verify if you have Python installed on you system using
```
python --version
```
or
```
python3 --version
```

If you are getting any sort of errors, just install it from https://www.python.org/downloads/

- Download the Anime watchlist from your preferred anime streaming site in Text (.txt) Format. 

- Rename that file to `export.txt`

## Installation 🛠️

1. Clone the repository or download it in zip format:

    ```
    git clone https://github.com/yourusername/animlist-exporter.git
    ```

## Usage ⚙️

To export your anime list to `MyAnimeList`, follow these steps:

1. Copy the Downloaded Anime watchlist text file and paste it in the cloned repository (or just downloaded folder if you downloaded the zip file).

2. Open any Terminal in this folder (Command Prompt / Powershell / Windows Terminal / any Linux Shell)

3. Run the tool with the following command:

    ```
    python script.py
    ```
    Try `python3` in place of `python` if  you are getting any errors.


4. After completion, go to the URL https://myanimelist.net/import.php and select `Import Type` as  `MyAnimeList Import`.

5. Choose the newly generated `anime_data.xml` file and upload it.

6. Enjoy your anime list on MyAnimeList!

# Note 🚨

This script adds the Anime into MAL with status `Plan to watch`, which means unfortunately you would have to manually set the status of each anime to `Watching` or `Completed` after importing.

This is due to aniwatch.to , hianime.to not providing the status of the anime in their export file. 

---