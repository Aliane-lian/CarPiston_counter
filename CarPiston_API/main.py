from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from collections import Counter
import tempfile
import shutil


app = FastAPI(title="Piston Detection API")

model = YOLO("best.pt")  

class_map = {0: "P1", 1: "P2", 2: "P3", 3: "P4"}

@app.post("/detect/")
async def detect_pistons(file: UploadFile = File(...)):
    try:
    
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        results = model(tmp_path)[0]
        class_ids = results.boxes.cls.tolist()
        labels = [class_map[int(i)] for i in class_ids]
        counts = Counter(labels)

        output = {label: counts.get(label, 0) for label in class_map.values()}
        return JSONResponse(content=output)

    except Exception as e:
        return JSONResponse(
            content={"error": "Detection failed", "details": str(e)},
            status_code=500
        )

@app.get("/")
def root():
    return {"message": "Piston detection server is running"}
