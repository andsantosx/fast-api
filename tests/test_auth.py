from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': user.clean_password,
        },
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'bearer'
    assert 'access_token' in token


def test_get_token_user_not_found(client):
    response = client.post(
        '/auth/token',
        data={
            'username': 'nonexistent@exemple.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'message': 'Usuário ou email inválido'}


def test_get_token_wrong_password(client, user):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': 'wrongpassword',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'message': 'Usuário ou email inválido'}
