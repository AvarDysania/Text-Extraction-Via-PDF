import PyPDF2
a=PyPDF2.PdfReader('Holy_Bible.pdf');
Empty="";
for i in range(1,16):
    Empty+=a.pages[i].extract_text();


with open("Text.txt","w",encoding="utf-8") as f:
    f.write(Empty);




