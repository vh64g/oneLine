"""
Theory:
abc = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
symbols = "!§$%&/()=?*+#;,:._-<>{}[]~"
chars = list(str(f"{abc}{abc.upper()}{nums}{symbols}"))
print(len(chars))
while a:=True:
    seed = int(input("Seed: "))
    key1 = abs(seed / -.899 * seed * 2.2222 * 3.9367 * 57.9939474 * 61365532)
    key2 = (seed / 2) * key1
    key_list1 = list(str(key1).replace(".", "").replace("e", "").replace("+", ""))
    key_list2 = list(str(key2).replace(".", "").replace("e", "").replace("+", ""))
    print(f"Keylist1: {key_list1}\nKeylist2: {key_list2}")
    pw_len = 8
    pw = ""
    for i in range(pw_len):
        pos = int(str(key_list1[i])+str(key_list2[i]))
        if pos>len(chars)-1: pos -= 80
        print(f"{i}:\n    Keylist1: {key_list1[i]}\n    Keylist2: {key_list2[i]}\n    Res: {pos}")
        pw+=chars[pos]
    print(chars)
    print(pw)
"""

while True: print(abc:="abcdefghijklmnopqrstuvwxyz",nums:="1234567890",symbols:="!§$%&/()=?*+#;,:._-<>{}[]~",chars:=list(str(f"{abc}{abc.upper()}{nums}{symbols}")), print(seed:=int(input("Seed: ")),key1:=abs(seed / -.899 * seed * 2.2222 * 3.9367 * 57.9939474 * 61365532),key2:=(seed / 2) * key1,key_list1:=list(str(key1).replace(".", "").replace("e", "").replace("+", "")),key_list2:=list(str(key2).replace(".", "").replace("e", "").replace("+", "")),pw_len:=8,ppos:=[int(str(key_list1[i])+str(key_list2[i])) for i in range(pw_len)],pos:=[el-80 if el>len(chars)-1 else el for el in ppos],pw_chars:=[chars[pos_e] for pos_e in pos], end="\r"),print(pw:="".join(pw_chars)), end="\r")
