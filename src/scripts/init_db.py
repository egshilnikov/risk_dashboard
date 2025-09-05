from models.database import Base, engine # pyright: ignore[reportMissingImports]
import models.portfolio  # import all model files

Base.metadata.create_all(bind=engine)