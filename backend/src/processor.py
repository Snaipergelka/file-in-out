import io


class ProcessImage:
    """
    Image processing class.
    """
    def __init__(self, image):
        self.image = image

    def get_size(self):
        size = io.BytesIO(self.image).getbuffer().nbytes
        return size
