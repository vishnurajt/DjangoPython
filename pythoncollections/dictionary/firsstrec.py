text="ABABABC"
dict={}
for ch in text:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is first recursive character")
        break


