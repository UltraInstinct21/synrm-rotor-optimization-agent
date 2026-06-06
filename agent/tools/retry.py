"""Retry + timeout utilities for node execution."""

import functools
import time
import threading


def retry(max_attempts: int = 2, delay: float = 2.0):
    """Decorator: retry a function up to max_attempts with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if attempt < max_attempts:
                        time.sleep(delay * (2 ** (attempt - 1)))
            raise last_error
        return wrapper
    return decorator


def timeout_node(func, args=(), kwargs=None, timeout_s: int = 120):
    """Run a node function with a timeout. Returns result or raises TimeoutError."""
    kwargs = kwargs or {}
    result = [None]
    exception = [None]

    def runner():
        try:
            result[0] = func(*args, **kwargs)
        except Exception as e:
            exception[0] = e

    thread = threading.Thread(target=runner, daemon=True)
    thread.start()
    thread.join(timeout_s)

    if thread.is_alive():
        raise TimeoutError(f"Node timed out after {timeout_s}s")
    if exception[0]:
        raise exception[0]
    return result[0]
