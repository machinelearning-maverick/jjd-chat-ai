from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import os

import importlib.resources as pkg_resources
import app.com.machinelearning.apps.useful.jjdchatai.services.posts_loader as pl
import app.com.machinelearning.apps.useful.jjdchatai.services.assemble_llm_data as ald

def prepare_vector_store(file_name=""):
    print(f"prepare_vector_store({file_name})")
    app_resources = os.environ["APP_WEB_RESOURCES_ROOT"]
    posts_csv_file = os.environ["BLOG_POSTS_FILE"]

    resource_path = pkg_resources.files(app_resources).joinpath(posts_csv_file)
    loaded_posts = pl.load_file(resource_path)
    chunks = ald.chunk_data(loaded_posts)
    vector_store = ald.create_embeddings(chunks)
    print("Vector store prepared")
    return vector_store
