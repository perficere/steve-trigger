import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from sentry_sdk.integrations.serverless import serverless_function

import env

from .trigger import main as trigger

sentry_sdk.init(dsn=env.SENTRY_DSN, integrations=[AwsLambdaIntegration(timeout_warning=True)], environment=env.STAGE)


trigger = serverless_function(trigger)
