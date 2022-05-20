text=input("File name: ").lower()
if '.gif' in text:
    print("image/gif")
elif '.png' in text:
    print("image/png")
elif '.jpg' in text:
    print("image/jpeg")
elif '.jpeg' in text:
    print("image/jpeg")
elif '.pdf' in text:
    print("application/pdf")
elif '.txt' in text:
    print("text/plain")
elif '.zip' in text:
    print("application/zip")

else:
    print("application/octet-stream")