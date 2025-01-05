from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import os
import streamlit as st

import importlib.resources as pkg_resources
import app.jjd_chat_ai.com.machinelearning.apps.useful.jjdchatai.services.posts_loader as pl

if __name__ == "__main__":
    app_resources = os.environ["APP_WEB_RESOURCES_ROOT"]
    posts_csv_file = "Wpisy-Export-2025-January-02-2137.csv"

    st.title("Question and Answer Chat")
    st.write("Question and Answer Chat for the Blog content - powered by AI")

    message = st.text_input("Write question:")
    clicked = st.button("Ask question")


def session_management():
    if "vs" not in st.session_state:
        resource_path = pkg_resources.files(app_resources).joinpath(posts_csv_file)
        loaded_posts = pl.load_file(resource_path)
        pass
