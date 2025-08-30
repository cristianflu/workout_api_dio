from fastapi import FastAPI
<<<<<<< HEAD
from fastapi_pagination import add_pagination
from app.routes import atleta_routes, categoria_routes, centro_routes
from app.core.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout API DIO")
=======
from app.routes import atleta_routes, categoria_routes, centro_routes
from fastapi_pagination import add_pagination

app = FastAPI(title="Workout API")
>>>>>>> d77197988fe1ecbbfc0cf9d0b601c92433871280

app.include_router(atleta_routes.router)
app.include_router(categoria_routes.router)
app.include_router(centro_routes.router)

add_pagination(app)
