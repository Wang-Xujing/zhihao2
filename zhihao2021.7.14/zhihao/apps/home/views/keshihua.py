from django.views import View
from django.http import JsonResponse
from apps.basic.models import BasicInfo
import datetime


class first_visual(View):
    def sort_data(self, data):
        data_sort = sorted(data.items(), key=lambda x: x[0].toordinal())
        return data_sort

    def get(self, request):
        context = {
            'status': 200
        }
        limit = request.GET.get('limit')
        range = request.GET.get('range')
        if range == 'all':
            data = {}
            for i in BasicInfo.objects.all():
                if i.birth in data:
                    data[i.birth] = data[i.birth] + 1
                else:
                    data[i.birth] = 1

            data_sort = self.sort_data(data)
            if limit == 'all':
                context['data'] = data_sort
            else:
                context['data'] = data_sort[:int(limit)]
            return JsonResponse(data=context)
        else:
            year=datetime.date(int(range),1,1)

            data = {}
            for i in BasicInfo.objects.filter(birth__gte=year):
                if i.birth in data:
                    data[i.birth] = data[i.birth] + 1
                else:
                    data[i.birth] = 1

            data_sort = self.sort_data(data)
            if limit == 'all':
                context['data'] = data_sort
            else:
                context['data'] = data_sort[:int(limit)]
            return JsonResponse(data=context)


class count_year(View):
    def get(self, request):
        basics = BasicInfo.objects.all()
        context = {
            'status': 200,
            'year':[]
        }
        for i in basics:
            if i.birth.year not in context['year']:
                context['year'].append(i.birth.year)
                print(i.birth.year)
            else:
                pass
        context['year'].sort()
        print(context['year'])
        return JsonResponse(data=context)
