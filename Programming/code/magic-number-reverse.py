with open("fl4g.jpeg", "rb") as file:
    BUF = 4    
    bytes_rev = b""
    bytes_read  = bytearray(file.read(BUF))

    while bytes_read:
        bytes_rev += bytes_read[::-1]
        bytes_read = file.read(BUF)
    with open("modified_fl4g.jpeg", "wb") as newfile:
        newfile.write(bytes_rev)
