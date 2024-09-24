formats = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}
name = input("File name: ").strip().lower()

if name.rfind(".") != -1:
    index = int(name.rindex(".")) + 1
    name2 = name[index:]
    if name2 in formats:
        print(formats[name2])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
