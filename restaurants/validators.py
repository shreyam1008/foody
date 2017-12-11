from django.core.exceptions import ValidationError

citys = ['kathmandu', 'bhaktapur', 'lalitpur', 'pokhara']
def validate_city(value):
    value = value.lower()
    if value not in citys:
        raise ValidationError("City not avilable")
