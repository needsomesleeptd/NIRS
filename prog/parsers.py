import fitz

class UnimplementedException(BaseException):
    pass
        
class Image:
    def __init__(self, ext: str, width: int, height: int, image: bytes):
        self._ext = ext
        self._width = width
        self._height = height
        self._image = image
    
    def get_ext(self) -> str:
        return self._ext
    
    def get_width(self) -> int:
        return self._width
    
    def get_height(self) -> int:
        return self._height
    
    def get_raw_bytes(self) -> bytes:
        return self._image
    

class Parser:
    def __init__(self, pdf_doc: fitz.Document):
        self._doc = pdf_doc
        
    def parse_text(self) -> str:
        text_each_page: list[str] = []
        for page in self._doc:
            text_each_page.append(page.get_textpage().extractText())
        return " ".join(text_each_page)

    def parse_images(self) -> list[Image]:
        img_each_page: list[Image] = []
        for page in self._doc:
            images_meta = page.get_images(full=True)
            for img in images_meta:
                xref = img[0]
                data = self._doc.extract_image(xref)
                img_each_page.append(
                    Image(data['ext'], data['width'], data['height'], data['image'])
                )
        return img_each_page
    
    def parse_tables(self):
        raise UnimplementedException
    
    def parse_formulas(self):
        raise UnimplementedException
         