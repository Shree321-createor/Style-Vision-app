import csv

from app.services.style_analysis_service import (
    StyleAnalysisService
)

analysis_service = StyleAnalysisService()

total = 0
correct = 0

with open(
    "eval/labels.csv",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        image_name = row["image_name"]

        expected = row[
            "expected_garment_type"
        ]

        result = analysis_service.analyze(
            f"sample_images/{image_name}"
        )

        predicted = result[
            "garment_type"
        ]

        total += 1

        if predicted == expected:
            correct += 1

        print(
            f"{image_name} | "
            f" | Description: {result['description']}"
            f" | Expected: {expected}"
            f" | Predicted: {predicted}"
        )

accuracy = (
    correct / total
) * 100

print(
    f"\nAccuracy: "
    f"{accuracy:.2f}%"
)
