from functools import wraps


def try_dec():
    def decorator(func):
        @wraps(func)
        async def result(*args: tuple, **kwargs: dict) -> None:
            try:
                return await func(*args, **kwargs)
            except Exception:
                pass

        return result

    return decorator
