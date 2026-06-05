from .database import Base
from datetime import datetime
from typing import List, Optional
from sqlalchemy import text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    published: Mapped[bool] = mapped_column(server_default='TRUE')
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text('now()')
    )


