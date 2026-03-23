from http import HTTPStatus

from fast_zero.database import get_session
from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    response_data = response.json()
    assert 'access_token' in response_data
    assert response_data['token_type'] == 'bearer'
    assert 'username' not in response_data


def test_create_user_username_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'another@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'message': 'Usuário já existe'}


def test_create_user_email_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'another',
            'email': 'alice@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'message': 'Email já existe'}


def test_read_users(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        '/users/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user_not_found(client, token):
    response = client.get(
        '/users/2',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'message': 'Not enough permissions'}


def test_update_user(client, user, token):
    response = client.put(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@exemple.com',
    }


def test_update_user_not_found(client, token):
    response = client.put(
        '/users/2',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'message': 'Not enough permissions'}


def test_delete_user(client, user, token):
    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuário deletado papito'}


def test_delete_user_not_found(client, token):
    response = client.delete(
        '/users/999',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'message': 'Not enough permissions'}


def test_update_integrity_error(client, user, token):
    response = client.post(
        '/users/',
        json={
            'username': 'fausto',
            'email': 'fausto@exemple.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'fausto',
            'email': 'bob@exemple.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'message': 'Usuário ou email já existe'}


def test_get_session():
    session = next(get_session())
    assert session is not None


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={
            'username': user.email,
            'password': user.clean_password,
        },
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'bearer'
    assert 'access_token' in token
