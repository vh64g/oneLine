
while True: y = int(input("[3n+1]Number?: ")) if (inp:=input("[3n+1]option?: "))=="n" else exec("while y > 1: print(y:=int(y/2)) if y % 2 == 0 else print(y:=int(3*y+1)) if y % 2 != 0 else print(y)") if inp.lower()=="calc" else exit() if inp.lower() in ["exit", "stop", "e", "esc"] else print("cmd not found")
