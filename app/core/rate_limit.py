import time
from collections import defaultdict
from fastapi import HTTPException, Request, status


class RateLimiter:
    def __init__(self, max_calls: int = 5, period: int = 60):
        self.max_calls = max_calls
        self.period = period
        self.requests: dict[str, list[float]] = defaultdict(list)

    def _cleanup(self, key: str):
        now = time.time()
        self.requests[key] = [
            t for t in self.requests[key] if now - t < self.period
        ]

    def check(self, key: str):
        self._cleanup(key)
        if len(self.requests[key]) >= self.max_calls:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Trop de tentatives. Réessayez dans une minute.",
            )
        self.requests[key].append(time.time())


login_limiter = RateLimiter(max_calls=5, period=60)


async def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"
