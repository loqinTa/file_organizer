import os
import shutil

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt", ".rtf", ".csv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Programs": [".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm", ".bat", ".sh"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".go", ".rs", ".json", ".xml", ".yaml"]
}

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in EXTENSIONS.items():
        if ext in extensions:
            return category
    return "Other"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return
    
    stats = {category: 0 for category in EXTENSIONS.keys()}
    stats["Other"] = 0
    total = 0
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            category = get_category(item)
            dest_folder = os.path.join(folder_path, category)
            create_folder(dest_folder)
            
            dest_path = os.path.join(dest_folder, item)
            shutil.move(item_path, dest_path)
            
            stats[category] += 1
            total += 1
            print(f"Moved: {item} -> {category}")
    
    print("\n=== REPORT ===")
    for category, count in stats.items():
        if count > 0:
            print(f"{category}: {count} files")
    print(f"Total: {total} files organized")

def main():
    print("=== FILE ORGANIZER ===")
    folder = input("Enter folder path (press Enter for Downloads): ").strip()
    
    if not folder:
        folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    print(f"Target folder: {folder}")
    organize_folder(folder)

if __name__ == "__main__":
    main()
