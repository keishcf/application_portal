from django import template
import re

register = template.Library()


@register.filter(name="mbs")
def bytes_to_megabytes(var):
    megabytes = var / (1024 * 1024)
    return f"{megabytes:.2f} mb"


@register.filter(name="pdf_name")
def extract_filename_from_url(url):
    # Use regex to extract the filename from the URL
    filename_match = re.search(r"/([^/]+)\.pdf$", url)

    if filename_match:
        filename = filename_match.group(1)
        # Replace hyphens with spaces and remove the leading digits and underscore
        filename = re.sub(r"^\d+-|_", " ", filename)
        return filename
    else:
        return None
