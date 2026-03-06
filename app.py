import streamlit as st
from rag import build_vectorstore, retrieve_context

st.title("Chat with your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    if "vectorstore" not in st.session_state:
        with st.spinner("Indexing PDF..."):
            st.session_state.vectorstore = build_vectorstore(uploaded_file)

    query = st.text_input("Ask a question about the PDF")

    if query:
        context, docs = retrieve_context(st.session_state.vectorstore, query)

        st.subheader("Retrieved context")
        st.write(context[:3000])

        st.subheader("Source pages")
        pages = sorted({d.metadata.get("page", "?") for d in docs})
        st.write(pages)

        # Replace this with any LLM call you want
        prompt = f"""
Answer the question using only the context below.
If the answer is not in the context, say you don't know.

Question:
{query}

Context:
{context}
"""
        st.subheader("Prompt for LLM")
        st.code(prompt)
