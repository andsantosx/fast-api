from dataclasses import asdict
from datetime import datetime

import pytest
from sqlalchemy import select

from fast_zero.database import get_session
from fast_zero.models import User


@pytest.mark.asyncio
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        await session.commit()

        user = await session.scalar(
            select(User).where(User.username == 'alice')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
        'todos': [],
    }


@pytest.mark.asyncio
async def test_update_user(session, mock_db_time):
    with mock_db_time(model=User):
        new_user = User(
            username='alice',
            email='alice@exemple.com',
            password='secret',
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        new_user.username = 'bob'
        await session.commit()
        await session.refresh(new_user)

    assert new_user.username == 'bob'
    assert isinstance(new_user.updated_at, datetime)


@pytest.mark.asyncio
async def test_get_session():
    session = get_session()
    assert await anext(session) is not None
