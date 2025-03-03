import streamlit as st
import docx
import PyPDF2

st.title("Natural Lnaguage to python Converter!")

def read_txt(file):
    return file.read().decode("utf-8")

def read_docx(file):
    doc=docx.Document(file)
    return "\n".join([token.text for token in doc.paragraphs])

def read_pdf(file):
    read=PyPDF2.PdfReader(file)
    return "\n".join([pge.extract_text() for pge in read.pages if pge.extract_text()])

st.title("Upload A Document : ")

file=st.file_uploader("upload your document",type=['txt','docx','pdf'])

if file is not None:
    file_type=file.name.split(".")[-1]

    if file_type=="txt":
        content=read_txt(file)
    elif file_type=="docx":
        content=read_docx(file)
    elif file_type=="pdf":
        content=read_pdf(file)
    else:
        print("Invalid File Format f{file_type} please use pdf,txt or docsx")

    st.subheader("Extracted Content:")
    st.text_area("Document Content", content, height=300)


