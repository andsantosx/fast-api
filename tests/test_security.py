from http import HTTPStatus

import jwt

from fast_zero.security import create_access_token


def test_jwt(set_settings):
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = jwt.decode(
        token, set_settings.SECRET_KEY, algorithms=[set_settings.ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.get(
        '/users/',
        headers={'Authorization': 'Bearer invalid_token'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'message': 'Could not validate credentials'}


def test_get_current_user_no_email(client):
    data = {'no_sub': 'test'}
    token = create_access_token(data)
    response = client.get(
        '/users/',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'message': 'Could not validate credentials'}


def test_get_current_user_user_not_found(client):
    data = {'sub': 'nonexistent@example.com'}
    token = create_access_token(data)
    response = client.get(
        '/users/',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'message': 'Could not validate credentials'}
