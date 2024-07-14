from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.solicitud_routes import router as solicitud_router
from routes.area_routes import router as area_router
from routes.rol_routes import router as rol_router
from routes.rolxusuario_routes import router as rolxusuario_router
from routes.atributo_routes import router as atributo_router
from routes.atributoxusuario_routes import router as atributoxusuario_router
from routes.soli_routes import router as soli_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

routes =  [
    user_router,
    solicitud_router,
    area_router,
    rol_router,
    rolxusuario_router,
    atributo_router,
    atributoxusuario_router,
    soli_router

]

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://soli-iub-front.onrender.com",
    "https://soli-iub-front.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(solicitud_router)
app.include_router(area_router)
app.include_router(rol_router)
app.include_router(rolxusuario_router)
app.include_router(atributo_router)
app.include_router(atributoxusuario_router)
app.include_router(soli_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)