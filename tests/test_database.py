from sqlalchemy import Engine
from src.database import engine

def test_engine_exists():
    assert engine is not None

def test_engine_is_sqlalchemy():
    assert isinstance(
        engine,
        Engine
    )
