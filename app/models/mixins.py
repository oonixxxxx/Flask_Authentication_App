from datetime import datetime
from app import db

class TimestampMixin:
    """Миксин для добавления временных меток"""
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SoftDeleteMixin:
    """Миксин для мягкого удаления"""
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    def soft_delete(self):
        """Мягкое удаление записи"""
        self.deleted_at = datetime.utcnow()
        db.session.commit() 