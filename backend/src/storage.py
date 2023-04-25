import os


class ImageStorage:
    def __init__(self):
        pass

    @staticmethod
    def list(directory):
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(subdir, file)
                img = open(filepath, "rb").read()
                yield img
