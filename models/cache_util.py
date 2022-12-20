from expiringdict import ExpiringDict


stores_cache = ExpiringDict(max_len=5000, max_age_seconds=60*60*24, items=None)
