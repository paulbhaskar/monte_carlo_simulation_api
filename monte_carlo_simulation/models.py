from datetime import datetime
from mongoengine import (DynamicDocument, fields)

# Create your models here.


class Trial(DynamicDocument):
    success = fields.BooleanField(default=False)
    created_at = fields.DateTimeField(default=datetime.utcnow)
    updated_at = fields.DateTimeField()
