"""API routes."""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/catalog")
async def get_catalog_info():
    try:
        return {
            "name": "iceberg",
            "type": "rest",
            "namespaces": ["default"],
            "warehouse_location": "/opt/iceberg-warehouse"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tables")
async def list_tables(namespace: Optional[str] = Query("default")):
    try:
        return {"namespace": namespace, "tables": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tables/{table_name}")
async def get_table(table_name: str):
    try:
        return {
            "name": table_name,
            "namespace": "default",
            "schema": {},
            "location": f"/opt/iceberg-warehouse/{table_name}"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/query")
async def execute_query(query: str):
    try:
        return {"success": True, "data": [], "execution_time_ms": 0}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/tables")
async def create_table(table_name: str, schema: dict):
    try:
        return {"success": True, "table": table_name, "created": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
