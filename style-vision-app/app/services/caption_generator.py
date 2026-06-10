from PIL import Image

from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)


class ImageCaptionGenerator:

    def __init__(self):

        self.processor = (
            BlipProcessor.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
        )

        self.model = (
            BlipForConditionalGeneration
            .from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
        )

    def produce_caption(
        self,
        image_path: str
    ):

        img = Image.open(
            image_path
        ).convert("RGB")

        inputs = self.processor(
            img,
            return_tensors="pt"
        )

        output = self.model.generate(
            **inputs,
            max_new_tokens=50
        )

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption
