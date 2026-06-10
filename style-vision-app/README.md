# Style Vision Catalog

## Project Overview

Style Vision Catalog is a full-stack fashion catalog application that allows users to upload garment images, automatically generate structured metadata with an AI model, and browse the catalog through a React frontend.

The app demonstrates an end-to-end flow for:

- Image upload and storage
- AI-powered caption generation
- Rule-based metadata extraction
- Catalog search and filtering
- Designer note support
- Evaluation and automated tests
- Frontend integration with a Vite React app

The backend is built with FastAPI and SQLite, while the frontend is implemented with React and TypeScript.

---

## Tech Stack

### Backend

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

### AI Components

- Hugging Face Transformers
- BLIP image captioning model
- PyTorch

### Frontend

- React
- TypeScript
- Vite
- Axios

### Testing

- Pytest
- FastAPI TestClient

---

## Project Structure

```
style-vision-app/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── catalog.py
│   │   │   └── notes.py
│   ├── database/
│   │   ├── db.py
│   │   └── dependencies.py
│   ├── models/
│   │   ├── clothing.py
│   │   └── designer_note.py
│   ├── schemas/
│   │   ├── clothing_schema.py
│   │   └── note_schema.py
│   ├── services/
│   │   ├── caption_generator.py
│   │   ├── attribute_extractor.py
│   │   └── style_analysis_service.py
│   └── main.py
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
├── tests/
├── eval/
│   ├── evaluate.py
│   └── labels.csv
├── uploads/
├── sample_images/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Design Approach

The architecture is intentionally simple and modular:

1. Users upload an image to the backend.
2. The backend stores the file in `uploads/`.
3. The BLIP captioning model generates a text description.
4. The caption is converted into structured fashion attributes by a rule-based extractor.
5. The metadata is persisted in SQLite.
6. The React frontend consumes the catalog API for listing, searching, filtering, and annotating items.

This separation keeps the API, service, database, and frontend layers easy to understand and extend.

---

## Running the Backend

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

## Running the Frontend

```bash
cd frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

Open the app in your browser:

```text
http://localhost:5173
```

---

## API Endpoints

### Catalog

| Method | Endpoint       | Description                                    |
| ------ | -------------- | ---------------------------------------------- |
| POST   | /items/upload  | Upload an image and create metadata            |
| GET    | /items         | List all catalog items                         |
| GET    | /items/search  | Search items by text                           |
| GET    | /items/filter  | Filter items by garment type, style, or season |
| GET    | /items/filters | Retrieve available filter values               |

### Designer Notes

| Method | Endpoint         | Description                    |
| ------ | ---------------- | ------------------------------ |
| POST   | /notes           | Add a designer note to an item |
| GET    | /notes/{item_id} | Retrieve notes for an item     |

### Health Check

| Method | Endpoint |
| ------ | -------- | ---------------- |
| GET    | /health  | Check API status |

---

## Testing

Run all tests:

```bash
pytest -v
```

If you want coverage:

```bash
pytest --cov=app
```

---

## Evaluation

The evaluation script compares predicted garment types against manually labeled examples in `eval/labels.csv`.

```bash
python -m eval.evaluate
```

The `sample_images/` folder contains test images used by the evaluation script.

---

## Challenges and Trade-offs

The main trade-off in this project was using a general-purpose BLIP captioning model as the source of truth for fashion metadata.

Because BLIP is not optimized for fashion classification, some captions describe the scene or the model rather than the garment itself. That means the downstream metadata extractor must be robust to noisy captions.

For this submission, a rule-based extractor was chosen because it is transparent, easy to test, and straightforward to debug.

---

## Future Improvements

- Replace BLIP with a fashion-specific model or fine-tune on garment data
- Improve metadata extraction with NLP or a learned classifier
- Add authentication and user profiles
- Move image storage to cloud object storage
- Replace SQLite with PostgreSQL
- Expand the evaluation dataset and metrics
- Improve frontend UX and filtering controls

---

## Notes

This project emphasizes correctness, maintainability, and clear separation of responsibilities over production-scale optimization. Each component is designed to be easy to understand and extend.
