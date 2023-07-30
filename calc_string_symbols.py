str = input()
cnt_C = str.upper().count("C")
cnt_G = str.upper().count("G")

print(((cnt_C + cnt_G) / len(str)) * 100)
