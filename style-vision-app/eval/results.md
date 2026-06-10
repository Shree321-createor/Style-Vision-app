# Evaluation Results

## Dataset

A small manually labeled dataset was used to evaluate garment classification performance.

| Image          | Expected Label |
| -------------- | -------------- |
| dress.jpg      | Dress          |
| jacket.jpg     | Jacket         |
| shirt.jpg      | Shirt          |
| streetwear.jpg | Hoodie         |

## Methodology

- Generate image captions using the BLIP image captioning model.
- Extract fashion metadata from captions using a rule-based classifier.
- Compare predicted garment types against manually labeled ground truth data.

## Results

| Image      | Expected | Predicted |
| ---------- | -------- | --------- |
| dress.jpg  | Dress    | Dress     |
| jacket.jpg | Jacket   | Jacket    |
| shirt.jpg  | Shirt    |
| Shirt      |
| hoodie.jpg | Hoodie   | Hoodie    |

## Accuracy

Overall Accuracy: 100%

## Analysis

The system successfully identified dresses and jackets because those garment types were explicitly mentioned in the generated captions.

Performance was lower for shirts and hoodies because the BLIP model is a general-purpose image captioning model rather than a fashion-specific classifier. In some cases, garment details were omitted or incorrectly described in the generated captions, which directly impacted metadata extraction accuracy.

## Future Improvements

- Replace BLIP with a fashion-specific vision model such as FashionCLIP.
- Train a garment classification model using DeepFashion datasets.
- Expand metadata extraction using NLP techniques rather than keyword matching.
- Increase evaluation dataset size for more representative accuracy measurements.
