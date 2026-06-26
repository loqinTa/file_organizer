# File Organizer

Python script that automatically organizes files in a folder by type.

## Features

- Scans any folder (default: Downloads)
- Moves files into subfolders based on extension
- Shows report after sorting

## Installation

git clone https://github.com/loginTa/file_organizer.git
cd file_organizer

## Usage

python main.py

Enter folder path or press Enter to use Downloads folder.

## Supported formats

- Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .ico, .tiff
- Documents: .pdf, .docx, .txt, .xlsx, .pptx, .odt, .rtf, .csv
- Music: .mp3, .wav, .aac, .flac, .ogg, .wma, .m4a
- Videos: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v
- Archives: .zip, .rar, .7z, .tar, .gz, .bz2, .xz
- Programs: .exe, .msi, .apk, .dmg, .deb, .rpm, .bat, .sh
- Code: .py, .js, .html, .css, .cpp, .java, .go, .rs, .json, .xml, .yaml

## Example output

Moved: photo.jpg -> Images
Moved: report.pdf -> Documents
Moved: song.mp3 -> Music

=== REPORT ===
Images: 1 files
Documents: 1 files
Music: 1 files
Total: 3 files organized

## Author

loqin
- Telegram: https://t.me/login_win
- Email: loqinkurator@gmail.com
