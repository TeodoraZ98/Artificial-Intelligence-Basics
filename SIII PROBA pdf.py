import PyPDF2
import textract  

filename="C:\User\ss\Desktop\JCUPUputstvo.pdf"
pdfOpen=open(filename,"rb")
pdfR=PyPDF2.PdfFileReader(pdfOpen)
