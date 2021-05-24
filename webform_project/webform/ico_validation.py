from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from lxml import etree
import requests

ARES_URL = 'https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico={}'


def ico_exists(ico: str):
    response = requests.get(ARES_URL.format(ico))
    if response.ok:
        root = etree.XML(response.text.encode("utf-8"))
        occurrences = root.xpath("//are:Pocet_zaznamu", namespaces=root.nsmap)
        if occurrences:
            occurrence_text = occurrences[0].text
            if occurrence_text.isnumeric():
                value = int(occurrence_text)
                if value != 1:
                    raise ValidationError('Enter a valid ico.')
            else:
                raise ValueError(f"API returned unexpected value: {occurrence_text}")
        else:
            raise ObjectDoesNotExist("Response doesn't contain required tag //are:Pocet_zaznamu")
    else:
        raise requests.exceptions.HTTPError(
            f"Request returned unexpected status code: {response.status_code} {response.text}"
        )
