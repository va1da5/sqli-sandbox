from datetime import datetime
from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import dependencies
from app.utils import simulate_network_latency

router = APIRouter()


@router.post("/create", response_model=schemas.User)
@simulate_network_latency
def user_create(
    *,
    db: Session = Depends(dependencies.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """Create a user"""
    new_user = models.User(
        username=user_in.username,
        created=datetime.now(),
        admin=user_in.admin,
    )
    db.add(new_user)
    db.commit()
    return new_user


@router.get("/list", response_model=List[schemas.User])
@simulate_network_latency
def user_get_list(*, db: Session = Depends(dependencies.get_db)) -> Any:
    """Get users list"""
    users = db.query(models.User).all()
    return users


@router.get("/details")
@simulate_network_latency
def user_get_details(*, db: Session = Depends(dependencies.get_db), id: str):
    """Get user details by id"""
    results_proxy = db.execute(f"select * from users where (id = '{id}')")
    return [{**row} for row in results_proxy]


@router.get("/exists", response_model=schemas.UserExists)
@simulate_network_latency
def user_exists(*, db: Session = Depends(dependencies.get_db), id: str):
    """Verify user existence by id"""
    results_proxy = db.execute(f"select * from users where (id = '{id}') limit 1")
    user_exists = bool(len(list(results_proxy)))
    return {"user_exists": user_exists}


@router.get("/blind", response_model=schemas.Message)
def user_blind_query(*, db: Session = Depends(dependencies.get_db), id: str):
    """Execute SQL query that does not return any values"""
    db.execute(f"select * from users where id = '{id}' limit 1")
    return {"msg": "Query executed. Response does not include results from database"}
