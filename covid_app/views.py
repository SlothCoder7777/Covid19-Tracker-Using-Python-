from django.shortcuts import render
from django.core.cache import cache
from .scraper import get_covid_data

def dashboard_view(request):
    search_query = request.GET.get('q', '').lower()
    data = cache.get('covid_data')
    if not data:
        data = get_covid_data()
        cache.set('covid_data', data, timeout=60 * 30)

    if search_query:
        data = [d for d in data if search_query in d["country"].lower()]
    top10 = sorted(data, key=lambda x: x['cases'], reverse=True)[:10]
    return render(request, 'dashboard.html', {"data": data, "top10": top10, "query": search_query})
