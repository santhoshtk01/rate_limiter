import time
import pytest
from rate_limiter.algorithms.token_bucket import TokenBucket

def test_token_bucket():
    bucket = TokenBucket(capacity=10, refill_rate=1)
    assert bucket.consume(5) == True
    assert bucket.consume(6) == False
    time.sleep(1)
    assert bucket.consume(6) == True