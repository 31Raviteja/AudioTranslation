from database.database import Base, engine
from database.models import Translation

Base.metadata.create_all(bind=engine)

print("✅ SQLite database created successfully.")