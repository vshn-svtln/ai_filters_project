
from PIL import Image


class Filter:
    def __init__(self, file_dir, dir_to_save):
        self.file_dir = file_dir
        self.dir_to_save = dir_to_save
    

class GrayFilter(Filter):
    def __init__(self, file_dir, dir_to_save):
        super().__init__(file_dir, dir_to_save)
    
    def gray_filter(self):
        image = Image.open(self.file_dir).convert('RGB')
        gray_image = image.convert('L')
        gray_image.save(self.dir_to_save)
        gray_image.show()