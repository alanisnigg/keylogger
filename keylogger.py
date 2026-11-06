def write_to_file():
    key = input("Metin gir: ")

    with open("key_log.txt", "a", encoding="utf-8") as f:
        f.write(key + "\n")

while True:
    write_to_file()