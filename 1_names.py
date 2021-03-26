from os import listdir

arr = listdir('.')
with open("song_names.txt", 'w', encoding="utf-8") as sn:
    for item in arr:
        if not (item.endswith(".py") or item.endswith(".txt")):
            sn.write(item + '\n')