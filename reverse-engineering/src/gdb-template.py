# https://rce4fun.blogspot.com/2014/09/nonconname-2014-inbincible-reversing.html
# to execute : gdb -x solve.py
import gdb

charset = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?_-@")
listflag = list("0000000000000000")
continue_num = 0
gdb.execute("file inbincible")
# break after returning from chanrecv
gdb.execute("b*0x08049118")
for i in range(0, 16):
    for j in charset:
        listflag[i] = j
        gdb.execute("run " + "".join(listflag))
        tmp = continue_num
        while tmp > 0:
            gdb.execute("c")
            tmp = tmp - 1
        # read the boolean value
        # If it's different in your case : dump $esp+0x1b upon breaking on the previous breakpoin
        b00l = gdb.execute("x/bx $esp+0x1b", to_string=True)
        if b00l[15] == "1":
            continue_num = continue_num + 1
            break
# print the flag
print("".join(listflag))
