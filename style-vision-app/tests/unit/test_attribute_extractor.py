from app.services.attribute_extractor import AttributeExtractor


def test_extracts_garment_type_color_and_style():
    extractor = AttributeExtractor()

    result = extractor.extract(
        "A blue floral dress for woman in a summer bohemian look with casual styling"
    )

    assert result["description"] == "A blue floral dress for woman in a summer bohemian look with casual styling"
    assert result["garment_type"] == "Dress"
    assert result["consumer_profile"] == "Women"
    assert result["color_palette"] == "Blue"
    assert result["pattern"] == "Floral"
    assert result["style"] == "Streetwear"
    assert result["season"] == "Summer"
    assert result["occasion"] == "Casual"
    assert result["trend_notes"] == "Modern streetwear trend"


def test_extracts_streetwear_and_falls_back_to_unknown_defaults():
    extractor = AttributeExtractor()

    result = extractor.extract(
        "A red hoodie with sneakers and casual streetwear vibes"
    )

    assert result["garment_type"] == "Hoodie"
    assert result["consumer_profile"] == "Unknown"
    assert result["color_palette"] == "Red"
    assert result["style"] == "Streetwear"
    assert result["season"] == "Winter"
    assert result["occasion"] == "Casual"
    assert result["trend_notes"] == "Modern streetwear trend"


def test_extract_returns_unknown_for_minimal_caption():
    extractor = AttributeExtractor()

    result = extractor.extract("A simple outfit")

    assert result["description"] == "A simple outfit"
    assert result["garment_type"] == "Unknown"
    assert result["style"] == "Unknown"
    assert result["material"] == "Unknown"
    assert result["pattern"] == "Unknown"
    assert result["color_palette"] == "Unknown"
    assert result["season"] == "Unknown"
    assert result["occasion"] == "Unknown"
    assert result["consumer_profile"] == "Unknown"
    assert result["trend_notes"] == ""
