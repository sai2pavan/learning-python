def main():
    file_name = input("Enter file name: ").strip()
    extension = file_name[-4:]
    print(mimetype(extension))

def mimetype(extension):
    match extension:
        case ".gif":
            return "image/gif"
        case "jpeg" | ".jpg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octec-stream"
        
main()