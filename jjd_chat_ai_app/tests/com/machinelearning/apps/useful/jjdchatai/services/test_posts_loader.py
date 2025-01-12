import os
import unittest

import importlib.resources as pkg_resources
import app.com.machinelearning.apps.useful.jjdchatai.services.posts_loader as pl
from dotenv import load_dotenv, find_dotenv


class PostLoaderTest(unittest.TestCase):
    LOADED_ELEMENTS = 2

    load_dotenv(find_dotenv(), override=True)
    app_test_resources = os.environ["APP_TEST_RESOURCES_ROOT"]
    test_post_txt_file = "test-posts.csv"


    def test_load_file(self):
        resource_path = pkg_resources.files(self.app_test_resources).joinpath(self.test_post_txt_file)
        data = pl.load_file(resource_path)

        self.assertEqual(self.LOADED_ELEMENTS, len(data))


if __name__ == '__main__':
    unittest.main()
