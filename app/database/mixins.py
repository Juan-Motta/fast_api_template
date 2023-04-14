from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    active = Column(Boolean, default=True)
