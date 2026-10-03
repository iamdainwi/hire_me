import logging

from app.core.config import settings

log = logging.getLogger(__name__)


def send_verification_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    log.info("verification link for %s: %s", to, link)  # swap for provider in Phase 5