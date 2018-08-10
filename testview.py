from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def aa():
    pass

@csrf_exempt
def test_func(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)
        import time
        resp = str(int(round(time.time() * 1000)))



        return JsonResponse(
            {"daku": resp}
        )


    return HttpResponseRedirect("")

