import os

def load_file(file_path):
    name, extension, = os.path.splitext(file_path)

    if extension == ".csv":
        from langchain_community.document_loaders import CSVLoader
        print(f"Loading a CSV file {file_path}")
        loader = CSVLoader(file_path)
    else:
        print("Document format is not supported")
        return None

    data = loader.load()
    return data
