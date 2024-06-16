import streamlit as st
import tiktoken
import docx

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def count_words(string: str) -> int:
    """Returns the number of words in a text string."""
    words = string.split()
    return len(words)

def read_docx(file):
    doc = docx.Document(file)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return '\n'.join(content)

def main():
    st.title("Word and Token Counter")
    st.caption("by [Yedidya Harris](https://www.linkedin.com/in/yedidya-harris/)")

    uploaded_file = st.file_uploader("Upload a DOCX or TXT file", type=["docx", "txt"])
    text_input = st.text_area("Or enter text here")

    if uploaded_file:
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            content = read_docx(uploaded_file)
    elif text_input:
        content = text_input
    else:
        content = ""

    if content:
        encoding_name = "o200k_base"  # for gpt-4o

        num_tokens = num_tokens_from_string(content, encoding_name)
        num_words = count_words(content)

        st.write(f"Number of tokens: {num_tokens}")
        st.write(f"Number of words: {num_words}")

if __name__ == "__main__":
    main()
