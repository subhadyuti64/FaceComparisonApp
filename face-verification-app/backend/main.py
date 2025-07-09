from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from face_utils import get_embedding_from_bytes, cosine_similarity
from models.detector import mtcnn
from models.embedder import facenet

app = FastAPI()

@app.post("/compare_faces/")
async def compare_faces(registered: UploadFile = File(...), current: UploadFile = File(...)):
    registered_bytes = await registered.read()
    current_bytes = await current.read()

    reg_emb, err1 = get_embedding_from_bytes(registered_bytes)
    cur_emb, err2 = get_embedding_from_bytes(current_bytes)

    if err1 or err2:
        return JSONResponse(status_code=400, content={
            "error": err1 or err2
        })

    score = cosine_similarity(reg_emb, cur_emb)
    threshold = 0.75
    result = "Verified: Same person" if score > threshold else "Mismatch: Not the same person"

    return {
        "similarity_score": round(score, 4),
        "result": result
    } 