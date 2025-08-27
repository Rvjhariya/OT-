from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn


app = FastAPI(title="OTSec API")


class Asset(BaseModel):
id: str
ip: str
vendor: Optional[str]=None
model: Optional[str]=None
firmware: Optional[str]=None
first_seen: datetime
last_seen: datetime


class Alert(BaseModel):
id: str
ts: datetime
severity: str
asset: Optional[str]=None
src: Optional[str]=None
title: str
details: dict = {}


DB_ASSETS = {}
DB_ALERTS = []


@app.get("/assets", response_model=List[Asset])
def list_assets():
return list(DB_ASSETS.values())


@app.get("/alerts", response_model=List[Alert])
def list_alerts():
return DB_ALERTS


if __name__ == "__main__":
uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)