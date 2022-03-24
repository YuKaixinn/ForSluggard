import img2pdf

pdf_file = "ImageToPdf/output/output.pdf"
img_file = "ImageToPdf/img/"
img_list = []

with open(pdf_file, "wb") as f:
    for i in range(1,22):
        img_list.append(img_file+str(i)+".png")
    f.write(img2pdf.convert(img_list))