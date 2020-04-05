import requests
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# script to iterate through many urls (leading to pdfs) that only change at the end

# array to save working urls
a = []
flag = "no flag yet";

# create and execute all get requests
for i in range(1,301):
    url = "url to exercise 5"
    # create url ending
    if (i > 99):
        url = url + str(i) + ".pdf"
    elif (i > 9):
        url = url + "0" + str(i) + ".pdf"
    elif(i<10):
         url = url + "00" + str(i) + ".pdf"
         print(url)

    # print progress
    print("nr.:" + str(i))

    # execute get request
    r = requests.get(url)

    # download all pdfs
    if r.status_code==200:
         save_to = "pdfs/number_" + str(i) + ".pdf"
         open(save_to, 'wb').write(r.content)
         a.append(i)

# analyse content of pdfs to find the flag
for i in a:
    pdf_url = "pdfs/number_" + str(i) + ".pdf"
    output_string = StringIO()
    with open(pdf_url, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    # this does not work (found the flag due to looking at the downloaded pdf's previews)
    if(output_string.getvalue().__contains__("flag")):
        print("it is " + pdf_url)


