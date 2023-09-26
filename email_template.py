from .email_app.models import EmailTemplate
birthday_template = EmailTemplate(
    template_type="birthday",
    subject="Happy Birthday!",
    body="Dear {{ user }},\n\nWishing you a very happy birthday!...",
)
birthday_template.save()

anniversary_template = EmailTemplate(
    template_type="anniversary",
    subject="Happy Anniversary!",
    body="Dear {{ user }},\n\nHappy anniversary to you and your spouse!...",
)
anniversary_template.save()

independence_day_template = EmailTemplate(
    template_type="independence_day",
    subject="Happy Independence Day!",
    body="Dear {{ user }},\n\nWishing you a joyful Independence Day!...",
)
independence_day_template.save()