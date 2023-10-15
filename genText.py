text = input("text to say: ")
export = ""

# 13,0,1,0,0,67.00;13,0,-1,0,0,;13,0,0,0,0,66.00???

charidx = 0-int(len(text)/2)-1

for char in text:
    charidx += 1
    converted_char = "13,0,"+str(charidx)+",0,0,;" if ord(char) == 65 else "13,0,"+str(charidx)+",0,0,"+ord(char)+".00"+";"
    export += converted_char

export = export[0:len(export)-1] # Trim off exceeding ";"
export += "???" # End register save

open("./output.txt","w").write(export)
