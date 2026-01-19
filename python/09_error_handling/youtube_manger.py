import json
filename = str("youtube.txt")

def load_data():
    try:
        with open(filename, "r") as file:
           return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(filename, "w") as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    print("\nList of all YouTube videos:")
    print("-" * 40)
    if not videos:
        print("No videos found.")
        return
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. Title: {video['title']}, URL: {video['duration']}, Description: {video['description']}")
    print("\n")
    print("-" * 40)


def add_video(videos):
    title = input("Enter video's title: ")
    duration = input("Enter video's duration: ")
    videos.append({"title": title, "duration": duration, "description": ""})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the number of the video to update: "))

    if( 1<= idx <= len(videos)):
        title = input("Enter new title (leave blank to keep current): ")
        duration = input("Enter new duration (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")

        if title:
            videos[idx - 1]['title'] = title
        if duration:
            videos[idx - 1]['duration'] = duration
        if description:
            videos[idx - 1]['description'] = description

        save_data_helper(videos)
    else:
        print("Invalid video number.")

def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the number of the video to delete: "))

    if( 1<= idx <= len(videos)):
        del videos[idx - 1]
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option:")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
