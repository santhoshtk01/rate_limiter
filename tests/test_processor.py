import pytest
from rate_limiter.processor import URLProcessor
from rate_limiter.exceptions import RateLimitExceeded, RobotsDisallowed

def test_rate_limit_exceeded():
    config = {
        "rate_limit": {
            "global_capacity": 1,
            "global_refill_rate": 1,
            "domain_capacity": 1,
            "domain_refill_rate": 1
        },
        "retry": {
            "max_retries": 1,
            "initial_delay": 1,
            "max_delay": 1
        },
        "concurrency": {
            "max_workers": 1
        },
        "proxies": [],
        "user_agent": "MyScraper/1.0"
    }
    processor = URLProcessor(config)
    urls = ["http://example.com"]
    with pytest.raises(RateLimitExceeded):
        processor.process_urls(urls * 2)