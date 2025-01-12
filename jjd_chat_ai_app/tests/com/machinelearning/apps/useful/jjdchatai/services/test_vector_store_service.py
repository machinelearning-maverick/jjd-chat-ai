import unittest

import jjd_chat_ai_app.app.com.machinelearning.apps.useful.jjdchatai.services.vector_store_service as vss

class Test(unittest.TestCase):
    def test_prepare_vector_store(self):
        vector_store = vss.prepare_vector_store()
        self.assertIsNotNone(vector_store)


if __name__ == '__main__':
    unittest.main()
