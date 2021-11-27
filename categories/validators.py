from django.core.exceptions import ValidationError


def validate_max_instance(obj):

    model = obj.__class__
    if (model.objects.count() >= 2000):
        raise ValidationError("Тhe maximum number of categories has been reached 2000")
