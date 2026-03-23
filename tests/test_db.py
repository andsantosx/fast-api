from dataclasses import asdict
from datetime import datetime

from sqlalchemy import select

from fast_zero.database import get_session
from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice',
            email='alice@exemple.com',
            password='secret',
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@exemple.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
    }


def test_update_user(session, mock_db_time):
    with mock_db_time(model=User):
        new_user = User(
            username='alice',
            email='alice@exemple.com',
            password='secret',
        )
        session.add(new_user)
        session.commit()

        new_user.username = 'bob'
        session.commit()
        session.refresh(new_user)

    assert new_user.username == 'bob'
    assert isinstance(new_user.updated_at, datetime)


def test_get_session():
    session = next(get_session())
    assert session is not None
