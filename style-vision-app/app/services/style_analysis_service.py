from app.services.caption_generator import ImageCaptionGenerator
from app.services.attribute_extractor import AttributeExtractor

caption_generator = ImageCaptionGenerator()
attribute_extractor = AttributeExtractor()


class StyleAnalysisService:

    def analyze(
        self,
        image_path: str
    ):

        caption = (
            caption_generator.produce_caption(
                image_path
            )
        )

        attributes = (
            attribute_extractor.extract(
                caption
            )
        )

        return attributes
