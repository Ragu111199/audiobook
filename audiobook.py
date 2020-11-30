
import PyPDF2
import pyttsx3



f = open('management_principles_tutorial.pdf','rb') # open the file in reading (rb) mode and call it f
f.seek(15,0)
pdf =PyPDF2.PdfFileReader(f) 
num_pages = pdf.numPages # store a text version of the pdf file f in pdf variable

play = pyttsx3.init()
print("Playing Audio Book!")

for num in range(0,num_pages):
    page = pdf.getPage(num)
    data = page.extractText()
    play.say(data)
    play.runAndWait()