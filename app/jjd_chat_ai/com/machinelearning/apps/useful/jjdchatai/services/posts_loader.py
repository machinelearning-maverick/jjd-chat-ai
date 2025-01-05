import os

def load_file(file):
    name, extension, = os.path.splitext(file)

    if extension == ".csv":
        from langchain.document_loaders import CSVLoader
        print(f"Loading a CSV file {file}")
        loader = CSVLoader(file)
    else:
        print("Document format is not supported")
        return None

    data = loader.load()
    return data
