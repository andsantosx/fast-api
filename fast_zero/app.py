from fastapi import FastAPI
from http import HTTPStatus

from fast_zero.schemas import Message

app = FastAPI(title='API de Estudos', description='API para estudos de FastAPI', version='0.1.0')


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message
)
def read_root():
    return {'message': 'Olá Mundo!'}
