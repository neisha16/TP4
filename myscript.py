import os

good_hash = os.environ.get("GOOD_HASH", "commit_bon")
bad_hash = os.environ.get("BAD_HASH", "commit_mauvais")

os.system("git bisect start $badhash $goodhash")
os.system("git bisect run python manage.py test")