# AI Virtual Stylist

An AI-powered fashion assistant that helps users choose outfits by analyzing body type, skin tone, and gender. 
It suggests clothing combinations based on style trends and offers a virtual try-on–ready pipeline, making shopping more personalized and convenient.

---

## Overview
This repository contains the core modules and a runnable scaffold for an AI Virtual Stylist.
It includes image-processing stubs, a recommendation API, and project documentation tailored for hiring teams (e.g., Telaverage).

> **Status:** In progress — this repo shows the architecture, core code skeleton, and a working demo endpoint. The roadmap below lists remaining items.

## Tech Stack
- **Languages:** Python
- **Libraries:** OpenCV, TensorFlow/Keras (placeholder), scikit-learn, Pillow
- **API Framework:** Flask
- **(Optional) Backend:** Firebase for storing user preferences and outfit metadata
- **OS:** Linux/Windows
- **Data Structures Used:** Arrays/Lists (feature vectors), Dictionaries/HashMaps (outfit attributes), Queues (image-processing workflow)

## Key Features
- Detect user attributes (body type, skin tone, gender) from an image *(stubs included)*
- Recommend outfit combinations using a rule-based/ML pipeline
- Simple REST API to get recommendations: `POST /recommend`
- Project documentation for recruiters

## Folder Structure
```
ai-virtual-stylist/
├─ src/
│  ├─ app.py                # Flask API (demo endpoint)
│  ├─ utils/
│  │  └─ image_processing.py
│  └─ models/               # (place your trained models here)
├─ data/
│  └─ samples/              # sample images (add your own)
├─ docs/
│  ├─ architecture.md
│  └─ screenshots/          # add screenshots of your UI/flow here
├─ .github/ISSUE_TEMPLATE/  # optional
├─ .gitignore
├─ requirements.txt
├─ LICENSE
├─ ROADMAP.md
└─ CONTRIBUTING.md
```

## How to Run (Demo API)
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # Linux/Mac: source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   python src/app.py
   ```
3. Test the endpoint in a new terminal:
   ```bash
   curl -X POST http://127.0.0.1:5000/recommend -H "Content-Type: application/json" -d "{\"image_path\": \"data/samples/user1.jpg\"}"
   ```

## Example Answers for Job Forms (Telaverage)
- **Role:** Project Lead & ML Developer
- **Programming Language(s):** Python
- **Frameworks/Libraries:** OpenCV, TensorFlow/Keras, Flask
- **Database:** Firebase (optional) or CSV/JSON for prototype
- **Data Structures:** Arrays/Lists (feature vectors), Dictionaries/HashMaps (attributes), Queues (processing pipeline)
- **Repo Link:** *(this GitHub URL after you upload)*

## Roadmap
See `ROADMAP.md` for a prioritized list of tasks suitable for internship/job discussions.

## License
MIT — see `LICENSE`.
