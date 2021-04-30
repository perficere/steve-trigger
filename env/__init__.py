import os
from pathlib import Path

############
# ENV VARS #
############

STAGE = os.environ.get("STAGE")

INTERNAL_KEY = os.environ.get("INTERNAL_KEY")
API_BASE_URL = os.environ.get("API_BASE_URL")

SENTRY_DSN = os.environ.get("SENTRY_DSN")


###################
# LOCAL OVERWRITE #
###################

LOCAL_STEM = "local"
LOCAL_PATH = Path(f"env/{LOCAL_STEM}.py")

if LOCAL_PATH.exists():
    from .local import *  # noqa: F401,F403
