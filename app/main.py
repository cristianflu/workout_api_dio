from fastapi import FastAPI
from app.routes import atleta_routes, categoria_routes, centro_routes
from fastapi_pagination import add_pagination

app = FastAPI(title="Workout API")

app.include_router(atleta_routes.router)
app.include_router(categoria_routes.router)
app.include_router(centro_routes.router)

add_pagination(app)
