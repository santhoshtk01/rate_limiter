from rate_limiter.processor import URLProcessor
from rate_limiter.algorithms.token_bucket import TokenBucket
from rate_limiter.utils import load_urls, load_config, unpickle_file

# Load URLs and configuration
urls = load_urls("urls.txt")
config = load_config("config.json")

# Initialize rate limiter and processor
rate_limiter = TokenBucket(
    capacity=config["rate_limit"]["domain_capacity"],
    refill_rate=config["rate_limit"]["domain_refill_rate"]
)
processor = URLProcessor(config)

# Process URLs
results = processor.process_urls(urls, headers=config.get("headers"))

# Save results (e.g., pickle or JSON)
import pickle
with open("results.pkl", "wb") as file:
    pickle.dump(results, file)

print(unpickle_file("results.pkl"))