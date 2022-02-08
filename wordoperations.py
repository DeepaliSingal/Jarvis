def read():
    pass
def write(n,name,drive):
    import docx
    mydoc = docx.Document()
    for i in range(n):
        mydoc.add_paragraph("This is first paragraph of a MS Word file.")
    mydoc.save(""+drive+":/"+name+".docx")