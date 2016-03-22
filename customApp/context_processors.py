from customApp.models import Partner


def partners_context_processor(request):
    return {"partners": Partner.objects.all()}
