import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    year = datetime.date.today().year
    if value > year:
        raise ValidationError('Проверьте год')
    return value
