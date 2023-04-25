from dependency_injector import containers, providers

from backend.config import get_settings
from backend.database.db import Database
from backend.database.connection.session import get_session
from backend.rqueue.connection.session import get_redis_connection
from backend.rqueue.rq import RedisQueue


class Container(containers.DeclarativeContainer):

    # used to store image analysis results
    session_maker = providers.Singleton(
        get_session, get_settings().database_uri)
    database = providers.Singleton(Database, session_maker)

    # used to queue tasks
    redis_connection_maker = providers.Singleton(
        get_redis_connection, *get_settings().redis_config
    )
    queue = providers.Singleton(RedisQueue, redis_connection_maker)
