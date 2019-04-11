from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import altair as alt
from .models import Solution


def my_cool_chart_view(req):
    # import ipdb; ipdb.set_trace()
    query = Solution.objects.all().values()
    data = alt.Data(values=list(query))
    chart_obj = alt.Chart(data).mark_bar().encode(
        alt.Y("sector:N"),
        alt.X('co2_reduction:Q'),
        alt.Color("solution:N",
            legend=None,
            scale=alt.Scale(scheme='tableau20')
        ),
        tooltip=["solution:N", 'co2_reduction:Q']
    )
    # import ipdb; ipdb.set_trace()
    return JsonResponse(chart_obj.to_dict(), safe=False)


# Create your views here.
def index(request):
    return render(request, "index.html", {})