from io import BytesIO 
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def applicant2pdf(template_source, context_dict={}):
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    applipdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,)
    # applipdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result,)
    if not applipdf.err:
        return HttpResponse(result.getvalue(), content_type = "application/pdf")
    return None

