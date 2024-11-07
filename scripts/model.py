from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Post:
    title: str
    url: str
    slug: str
    description: str
    tags: list[str]
    image: Optional[str]
    timestamp: datetime
