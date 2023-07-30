# create compressor
# examples:
# aaaabbcaa => a4b2c1a2
#
# abc => a1b1c1

s = input()
str = ""
cnt = 1

for i in range(len(s)):
  if (i+1 < len(s)) and s[i] == s[i+1]:
    cnt += 1
  else:
    print(s[i], end="")
    print(cnt, end="")
    cnt = 1


