import re
from rest_framework.serializers import ValidationError


class LinkValidator:
    """
    Валидатор для ссылок
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^https?://(?:www\.)?youtube\.com/.+$')
        tmp_val = dict(value).get(self.field)
        try:
            if not bool(reg.match(tmp_val)):
                raise ValidationError('Должна быть ссылка на youtube.com')
        except SyntaxError:
            print('SyntaxError')
        except TypeError:
            print('TypeError')
