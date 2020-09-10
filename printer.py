html = [
    "<html><head><style>.lines{width:100%;height:18.8px;float:left}#paper{background:white;background-image:url('images/paper.jpg');background-repeat: no-repeat;background-size: contain;float:left;padding:50px 50px;width:50%;height:80%}img,span{height:13px;width:9px;float:left;margin-top:8px;}</style></head><body><div id='paper'>"]

fhand = open("edited.txt", "r")
for line in fhand:
        word = line.strip()
        html.append('<div class="lines">')
        for ch in word:
            code = ord(ch)
            if (code==32):
                html.append("<span></span>")
            if(code>=33 and code<=64):
                letterType="numAndSpCh"
            if(code>=65 and code<=90):
                letterType="capital"
            if(code>=97 and code<=122):
                letterType="small"
            html.append("<img src='images/letters/{}/{}.png'/>".format(letterType, code))
        html.append("</div>")
fhand.close()
html.append("</div></body></html>")
paper=open('paper.html', 'w')
paper.writelines(html)

