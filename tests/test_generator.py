import os
import shutil
import unittest

from mlskeleton.generator import generate_folder_structure


class TestGenerateFolderStructure(unittest.TestCase):
    def setUp(self):
        self.root_folder = "test_folder"
        self.json_file_path = "test_folder_structure.json"

        # Create the test folder structure JSON file
        with open(self.json_file_path, "w") as f:
            f.write(
                '''{
                    "folder_1": {
                        "file_1.txt": {},
                        "folder_2": {
                            "file_2.txt": {}
                        }
                    },
                    "file_3.txt": {},
                    "folder_3": {}
                }'''
            )

    def tearDown(self):
        # Remove the test folder and JSON file
        shutil.rmtree(self.root_folder)
        os.remove(self.json_file_path)

    def test_generate_folder_structure(self):
        # Generate the test folder structure
        generate_folder_structure(self.root_folder, self.json_file_path)

        # Check that the root folder was created
        self.assertTrue(os.path.exists(self.root_folder))

        # Check that all the folders and files were created
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "folder_1")))
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "folder_1", "folder_2")))
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "folder_1", "file_1.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "folder_1", "folder_2", "file_2.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "file_3.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.root_folder, "folder_3")))

if __name__ == "__main__":
    unittest.main()