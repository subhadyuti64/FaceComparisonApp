from PIL import Image
import torch
import torch.nn.functional as F
import io
from models.detector import mtcnn
from models.embedder import facenet

def get_embedding_from_bytes(image_bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        face = mtcnn(img)
        if face is None:
            return None, "No face detected"
        with torch.no_grad():
            emb = facenet(face.unsqueeze(0)).squeeze()
        return emb, None
    except Exception as e:
        return None, str(e)

def cosine_similarity(emb1, emb2):
    return F.cosine_similarity(emb1.unsqueeze(0), emb2.unsqueeze(0)).item() 