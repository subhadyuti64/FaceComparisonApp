Face Verification App
A simple face verification system using FastAPI (backend) and Streamlit (frontend).

Project Structure
face-verification-app/
│
├── backend/                      # FastAPI backend
│   ├── main.py                   # FastAPI entry point
│   ├── face_utils.py             # Helper functions (embedding, similarity, etc.)
│   ├── models/                   # Pretrained model loaders
│   │   ├── detector.py           # MTCNN loader
│   │   ├── embedder.py           # FaceNet loader
│   └── requirements.txt          # Backend dependencies
│
├── frontend/                     # Streamlit frontend
│   ├── app.py                    # Streamlit UI
│   └── requirements.txt          # Frontend dependencies
│
├── data/                         # Sample/test images (optional)
│   ├── registered.jpg
│   └── current.jpg
│
├── README.md                     # Project overview
└── .gitignore                    # Common ignores (e.g., __pycache__, *.pt)
Usage
Backend
Install dependencies:
cd backend
pip install -r requirements.txt
Run the FastAPI server:
uvicorn main:app --reload
Frontend
Install dependencies:
cd frontend
pip install -r requirements.txt
Run the Streamlit app:
streamlit run app.py
Notes
Place sample images in the data/ folder for testing.
Update API_URL in frontend/app.py if backend is hosted remotely.
