import redis
from django.core.cache import caches
from cloud_storage.settings import env


class RedisTokenStorage:
    def __init__(self):
        self.cache = caches["jwt"]

    def save_refresh_token(self, user_id, jti, token, exp_seconds):
        """
        Сохраняем токен в redis
        Все параметры достаются из сгенерированного токена при логине.
        """
        key = f"jwt:refresh:{user_id}:{jti}"
        self.cache.set(key, token, timeout=exp_seconds)

    def is_refresh_token_valid(self, user_id, jti):
        key = f"jwt:refresh:{user_id}:{jti}"
        return self.cache.get(key) is not None

    def remove_refresh_token(self, user_id, jti):
        key = f"jwt:refresh:{user_id}:{jti}"
        self.cache.delete(key)

    def get_refresh_token_from_storage(self, user_id, jti):
        key = f"jwt:refresh:{user_id}:{jti}"
        return self.cache.get(key)

    @staticmethod
    def _get_all_tokens():
        r = redis.Redis(
            host=env("REDIS_HOST"),
            port=env("REDIS_PORT"),
            db=1
        )
        keys = r.keys()
        print(keys)

