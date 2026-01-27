import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY ,
               title TEXT NOT NULL,
               time TEXT NOT NULL,
               description TEXT
    )
''')


def list_all_videos():
    cursor.execute(''' SELECT * FROM videos ''')
    for row in cursor.fetchall():
        print(row)

def add_video():
    title = input("Enter Video Title: ")
    time = input("Enter Video Time: ")
    description = input("Enter Video description (option): ")
    cursor.execute(''' INSERT INTO videos ( title, time, description ) VALUES ( ?, ?, ? ) ''', ( title, time, description))
    conn.commit()

def update_video():
    idx = input("Enter video ID to update: ")
    new_title = input("Enter video Title (leave blank to keep current): ")
    new_time = input("Enter video Time (leave blank to keep current): ")
    new_description = input("Enter video new description (leave blank to keep current): ")
    cursor.execute(''' UPDATE videos SET title = ?, time = ?, description = ?,  WHERE ID = ? ''', (new_title, new_time, new_description, idx))
    conn.commit()

def delete_video():
    idx = input("Enter video ID to delete: ")
    cursor.execute(''' DELETE FROM videos where id = ? ''', {idx, })
    conn.commit()

def main():
    while True:
        print('\n Youtube manager app with DB')
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit')
        choice = input('Choice option from (1-5): ')

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close() # house keeping ( not corrupt the data in db )

if __name__ == '__main__':
    main()