class AttributeExtractor:

    def extract(self, caption: str):

        text = caption.lower()

        attributes = {
            "description": caption,
            "garment_type": "Unknown",
            "style": "Unknown",
            "material": "Unknown",
            "color_palette": "Unknown",
            "pattern": "Unknown",
            "season": "Unknown",
            "occasion": "Unknown",
            "consumer_profile": "Unknown",
            "trend_notes": "",
            "continent": "Unknown",
            "country": "Unknown",
            "city": "Unknown"
        }

        if "dress" in text:
            attributes["garment_type"] = "Dress"

        elif "jacket" in text:
            attributes["garment_type"] = "Jacket"

        elif "shirt" in text:
            attributes["garment_type"] = "Shirt"

        elif "hoodie" in text:
            attributes["garment_type"] = "Hoodie"

        elif "sweatshirt" in text:
            attributes["garment_type"] = "Sweatshirt"

        elif "pants" in text:
            attributes["garment_type"] = "Pants"

        elif "trousers" in text:
            attributes["garment_type"] = "Trousers"

        elif "jeans" in text:
            attributes["garment_type"] = "Jeans"

        elif "skirt" in text:
            attributes["garment_type"] = "Skirt"

        elif "coat" in text:
            attributes["garment_type"] = "Coat"

        elif "blazer" in text:
            attributes["garment_type"] = "Blazer"

        elif "sneakers" in text:
            attributes["garment_type"] = "Sneakers"

        elif "shoes" in text:
            attributes["garment_type"] = "Shoes"

        if "woman" in text:
            attributes["consumer_profile"] = "Women"

        elif "man" in text:
            attributes["consumer_profile"] = "Men"

            if attributes["garment_type"] == "Unknown":
                attributes["garment_type"] = "Shirt"
                attributes["style"] = "Casual"

        elif "girl" in text:
            attributes["consumer_profile"] = "Girls"

        elif "boy" in text:
            attributes["consumer_profile"] = "Boys"

        color_list = [
            "black",
            "white",
            "blue",
            "red",
            "green",
            "yellow",
            "pink",
            "purple",
            "orange",
            "brown",
            "grey",
            "gray"
        ]

        matched_colors = []

        for color in color_list:
            if color in text:
                matched_colors.append(color.title())

        if matched_colors:
            attributes["color_palette"] = ", ".join(matched_colors)

        if "floral" in text:
            attributes["pattern"] = "Floral"

        elif "striped" in text:
            attributes["pattern"] = "Striped"

        elif "checked" in text:
            attributes["pattern"] = "Checked"

        elif "plaid" in text:
            attributes["pattern"] = "Plaid"

        elif "printed" in text:
            attributes["pattern"] = "Printed"

        if "denim" in text:
            attributes["material"] = "Denim"

        elif "cotton" in text:
            attributes["material"] = "Cotton"

        elif "leather" in text:
            attributes["material"] = "Leather"

        elif "wool" in text:
            attributes["material"] = "Wool"

        elif "linen" in text:
            attributes["material"] = "Linen"

        if any(word in text for word in [
            "hoodie",
            "sneakers",
            "street",
            "casual"
        ]):
            attributes["style"] = "Streetwear"

        elif any(word in text for word in [
            "dress",
            "floral"
        ]):
            attributes["style"] = "Bohemian"

        elif any(word in text for word in [
            "blazer",
            "formal",
            "suit"
        ]):
            attributes["style"] = "Formal"

        if "field" in text:
            attributes["occasion"] = "Outdoor"

        elif "office" in text:
            attributes["occasion"] = "Work"

        elif "party" in text:
            attributes["occasion"] = "Party"

        elif "casual" in text:
            attributes["occasion"] = "Casual"

        if any(word in text for word in [
            "coat",
            "hoodie",
            "sweater",
            "wool"
        ]):
            attributes["season"] = "Winter"

        elif any(word in text for word in [
            "dress",
            "linen"
        ]):
            attributes["season"] = "Summer"

        if attributes["style"] == "Streetwear":
            attributes["trend_notes"] = (
                "Modern streetwear trend"
            )

        elif attributes["style"] == "Bohemian":
            attributes["trend_notes"] = (
                "Bohemian fashion trend"
            )

        elif attributes["style"] == "Formal":
            attributes["trend_notes"] = (
                "Classic formal wear trend"
            )

        return attributes
