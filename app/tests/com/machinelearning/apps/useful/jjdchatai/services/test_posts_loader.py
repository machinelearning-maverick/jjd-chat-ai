import os
import importlib.resources as pkg_resources
import app.jjd_chat_ai.com.machinelearning.apps.useful.jjdchatai.services.posts_loader as pl
from dotenv import load_dotenv, find_dotenv
from unittest import TestCase


class PostLoaderTest(TestCase):
    LOADED_ELEMENTS = 2

    load_dotenv(find_dotenv(), override=True)
    app_test_resources = os.environ["APP_TEST_RESOURCES"]
    test_post_txt_file = "test-posts.csv"

    def test_load_file(self):
        resource_path = pkg_resources.files(self.app_test_resources).joinpath(self.test_post_txt_file)
        print(f"app_test_resources: {resource_path}")
        data = pl.load_file(resource_path)
        print(f"data: {data}")

        self.assertEqual(self.LOADED_ELEMENTS, len(data))
