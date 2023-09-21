import gdb, string

gdb.execute("file ./challenge")
gdb.execute("set pagination off")
gdb.execute("set confirm off")
gdb.execute("b *0x4012C5")


success = [f"0x%.2x" % i for i in range(0x4045A0, 0x4045A0 + (43 * 384), 384)]

FLAG_LEN = 43

pattern = string.printable
known_flag = "Flag{"


def write_txt(val):
    with open("attempt.txt", "w") as f:
        f.write(val)


def write_end(val):
    with open("end.txt", "w") as f:
        f.write(val)


write_end(str(len(known_flag)))

while len(known_flag) != FLAG_LEN:
    for i, char in enumerate(pattern):
        bf = known_flag + char + "a" * (FLAG_LEN - len(known_flag) - 2) + "}"
        end = int(open("end.txt", "r").read())
        write_txt(bf)
        gdb.execute("run < attempt.txt > /dev/null")

        for _ in range(end):
            gdb.execute("continue")

        rax = int(gdb.execute("x/wx $rax", to_string=True).split()[-1], 16)
        if rax == int(success[end], 16):
            known_flag += char
            end += 1
            print("Correct:", bf)
            write_end(str(end))
            gdb.execute("kill")
            break
        else:
            print("Wrong:", bf)
            gdb.execute("kill")

print("done", bf)
