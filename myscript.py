import os

good_hash = os.environ.get("GOOD_HASH", "commit_bon")
bad_hash = os.environ.get("BAD_HASH", "commit_mauvais")

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")