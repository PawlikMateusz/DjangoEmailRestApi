# try:
#     message = create_message(data, email)
#     message.send()
#     email.send_date = datetime.now(tz=timezone.utc)
#     email.save()
#     logger.debug(
#         f"Email successfully sent from mailbox")
# except Exception as exc:
#     logger.debug("Error during sending email")
#     raise self.retry(max_retries=3, default_retry_delay=5, exc=exc)
