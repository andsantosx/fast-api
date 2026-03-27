from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from fast_zero.routers import auth, common, todos, users

app = FastAPI(
    title='API de Estudos', description='API para estudos de FastAPI'
)

app.include_router(common.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.detail},
    )
