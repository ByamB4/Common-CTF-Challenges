string_code = ["system", "id"]
obfuscated_code = ""
charset = "1234567890!#$%&'()*+/^,-.:;<=>?@[]_{|}~"

for code in string_code:
    obfuscated = ""
    for i in code:
        is_found_obfuscated = False
        for j in charset:
            for k in charset:
                if ord(j) ^ ord(k) == ord(i):
                    is_found_obfuscated = True
                    obfuscated += ".('%s'^'%s')" % (j, k)
                if is_found_obfuscated:
                    break
            if is_found_obfuscated:
                break
        if not is_found_obfuscated:
            obfuscated += ".'%s'" % i
    obfuscated_code += "(%s)" % obfuscated[1:]
print("".join(['("%s")' % i for i in string_code]) + "=" + obfuscated_code)
