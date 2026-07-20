import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

API_URL = os.getenv("API_URL")

st.set_page_config(
    page_title = "AI Document(Q&A Assistant)",
    page_icon = "📄",
    layout = "wide"
)

st.title("📄 AI Document Q&A Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("Upload your documents and ask questions.")

uploaded_files = st.file_uploader(
    "Upload a document",
    type=["pdf", "txt", "json", "docx"],
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Upload Files"):

        for uploaded_file in uploaded_files:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }
            
            with st.spinner(
                f"Uploading {uploaded_file.name}..."
            ):


                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

            if response.status_code == 200:

                data = response.json()

                st.success(
                    f"{uploaded_file.name} uploaded successfully"
                )

                st.write(
                    f"Chunks created: {data.get('total_chunks')}"
                )

            else:

                st.error(
                    f"Failed: {uploaded_file.name}"
                )


st.divider()

st.header("💬 Chat")


# Display previous messages
for message in st.session_state.messages:

    if message["role"] == "user":

        st.chat_message("user").write(
            message["content"]
        )

    else:

        st.chat_message("assistant").write(
            message["content"]
        )



question = st.chat_input(
    "Ask something about your documents..."
)



if question:

    # Save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.chat_message("user").write(
        question
    )

    with st.spinner("Thinking..."):

        response = requests.post(
            f"{API_URL}/chat",
            json={
                "question": question
            }
        )

    if response.status_code == 200:

        data = response.json()

        answer = data["answer"] 

        # Save assistant answer

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        with st.chat_message("assistant"):

            st.markdown(answer)

            if data.get("sources"):

                st.subheader("📚 Sources")

                for source in data["sources"]:

                    st.write(
                        f"📄 {source['Filename']} | Chunk {source['chunk_id']}"
                    )

    else:
        
        st.error(response.text)

with st.sidebar:

    st.header("Settings")   

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

with st.sidebar:

    st.header("📂 Uploaded Files")

    response = requests.get(
        f"{API_URL}/documents"
    )

    if response.status_code == 200:
        
        documents = response.json()['documents']

        if documents:

            for file in documents:
                st.write(f"✅ {file}")

        else:

            st.info("No document Uploaded")

    else:

        st.error("Cannot fetch documents.")