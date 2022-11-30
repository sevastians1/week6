from django.core.exceptions import ValidationError
from django.utils import timezone
def validate_date(year):
    if year<1900:
        raise ValidationError(f"We're not selling a car made in {year}")
    elif year >timezone.now().year+1:
        raise ValidationError(f"You can't sell a car made in the future")

