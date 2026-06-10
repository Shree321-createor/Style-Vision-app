from app.services import style_analysis_service
from app.services.style_analysis_service import StyleAnalysisService


class DummyCaptionGenerator:
    def produce_caption(self, image_path: str):
        return "A denim jacket for man with a striped design"


def test_analyze_uses_caption_generator_and_attribute_extractor(monkeypatch):
    monkeypatch.setattr(
        style_analysis_service,
        "caption_generator",
        DummyCaptionGenerator()
    )

    service = StyleAnalysisService()
    result = service.analyze("ignored/path.jpg")

    assert result["description"] == "A denim jacket for man with a striped design"
    assert result["garment_type"] == "Jacket"
    assert result["consumer_profile"] == "Men"
    assert result["material"] == "Denim"
    assert result["pattern"] == "Striped"
    assert result["style"] == "Unknown"
    assert result["season"] == "Unknown"
    assert result["occasion"] == "Unknown"
