from .models import HitCount


def hit_count_middleware(get_response):

    def middleware(request):
        # response = get_response(request)

        hc, created = HitCount.objects.get_or_create(path=request.path)
        if not created:
            hc.hits += 1
        hc.save()

        response = get_response(request)  # подсчитать любые обращения, в том числе и некорректные
        return response

    return middleware

