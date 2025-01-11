from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import os
import streamlit as st

import importlib.resources as pkg_resources
import app.com.machinelearning.apps.useful.jjdchatai.services.posts_loader as pl
import app.com.machinelearning.apps.useful.jjdchatai.services.assemble_llm_data as ald


def session_management():
    app_resources = os.environ["APP_WEB_RESOURCES_ROOT"]
    posts_csv_file = "Wpisy-Export-2025-January-02-2137.csv"

    if "vs" not in st.session_state:
        print(f"session_management()")
        resource_path = pkg_resources.files(app_resources).joinpath(posts_csv_file)
        loaded_posts = pl.load_file(resource_path)
        chunks = ald.chunk_data(loaded_posts)
        vector_store = ald.create_embeddings(chunks)
        st.session_state.vs = vector_store
        print("Session state created")


if __name__ == "__main__":
    app_resources = os.environ["APP_WEB_RESOURCES_ROOT"]
    posts_csv_file = "Wpisy-Export-2025-January-02-2137.csv"

    session_management()

    st.title("Question and Answer Chat")
    st.write("Question and Answer Chat for the Blog content - powered by AI")

    question = st.text_input("Write question:")
    clicked = st.button("Ask question")

    if clicked:
        llm_answer = ald.ask_and_get_answer(st.session_state.vs, question)
        answer = st.text_area("Answer:", value=llm_answer)
