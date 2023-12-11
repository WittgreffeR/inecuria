import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .dotenv import env

if env.bool("INTEGRATE_WITH_SENTRY", default=False):
    sentry_sdk.init(
        dsn=env("SENTRY_DSN"),
        integrations=[
            LoggingIntegration(
                level=env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO),
                event_level=logging.ERROR,
            ),
            DjangoIntegration(),
        ],
        environment=env.str("ENVIRONMENT", default="production"),
        traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),
    )
