from app import models, schemas
from app.api.dependencies import get_db

from .controller import controller as ws


@ws.event("user.list")
def user_get_list():
    db = next(get_db())
    users = db.query(models.User).all()
    return [schemas.User.from_orm(user).dict() for user in users]


@ws.event("user.details")
def user_get_list(*, id: str = None, **kwargs):
    db = next(get_db())
    results_proxy = db.execute(f"select * from users where (id = '{id}')")
    return [{**row} for row in results_proxy]


@ws.event("user.exists")
def user_exists(*, id: str = None, **kwargs):
    db = next(get_db())
    """Verify user existence by id"""
    results_proxy = db.execute(f"select * from users where (id = '{id}') limit 1")
    user_exists = bool(len(list(results_proxy)))
    return {"user_exists": user_exists}
