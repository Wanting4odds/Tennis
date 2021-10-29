import xlrd
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ResultsDataSerializer
from .models import ResultsData, add_data_from_xls
from django.views.decorators.csrf import csrf_exempt


def parse_file(book):
    """
    parse book data and create dict to map the data sync up to db later
    :param book: xls file data object
    :return: dict
    """
    sh = book.sheet_by_index(0)
    cases = []
    nrows = sh.nrows
    for rx in range(1, nrows):
        value = sh.row_values(rx)
        for v in range(len(value)):
            if value[v] == '':
                value[v] = None
        datetime_date = xlrd.xldate_as_datetime(value[3], 0)
        date_object = datetime_date.date()
        string_date = date_object.isoformat()
        cases.append(
          {
            'atp': value[0],
            'location': value[1],
            'tournament': value[2],
            'date': string_date,
            'series': value[4],
            'court': value[5],
            'surface': value[6],
            'round': value[7],
            'best_of': value[8],
            'winner': value[9],
            'loser': value[10],
            'wrank': value[11],
            'lrank': value[12],
            'wPts': value[13],
            'lpts': value[14],
            'w1': value[15],
            'l1': value[16],
            'w2': value[17],
            'l2': value[18],
            'w3': value[19],
            'l3': value[20],
            'w4': value[21],
            'l4': value[22],
            'w5': value[23],
            'l5': value[24],
            'wsets': value[25],
            'lsets': value[26],
            'comment': value[27],
            'b365w': value[28],
            'b365l': value[29],
            'exw': value[30],
            'exl': value[31],
            'lbw': value[32],
            'lbl': value[33],
            'psw': value[34],
            'psl': value[35],
            'sjw': value[36],
            'sjl': value[37],
            'maxw': value[38],
            'maxl': value[39],
            'avgw': value[40],
            'avgl': value[41]
          }
        )
    return cases


@csrf_exempt
def upload_file(request, template_name='file.html'):
    if request.method == 'POST':
        file_obj = request.FILES['result_data']
        book = xlrd.open_workbook(file_contents=file_obj.read())
        cases = parse_file(book)
        add_data_from_xls(cases=cases)
    else:
        pass
    return render(
      request,
      template_name=template_name
    )


class ResultsApiView(APIView):
    """
    List all results of tennis or create a new result
    """
    def get(self, request):
        all_data = ResultsData.objects.all().values()
        return Response({"Message": "List of Tennis Result",
                         "Results of Tennis": all_data})

    def post(self, request):
        serializer = ResultsDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ResultDetail(APIView):
    """
    Retrieve, update or delete a Result instance
    """
    def get_object(self, pk):
        try:
            return ResultsData.objects.get(pk=pk)
        except ResultsData.DoesNotExist:
            return Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = ResultsDataSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk):
        result = self.get_object(pk)
        serializer = ResultsDataSerializer(instance=result, data=request.data)
        print(serializer.error_messages)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.error_messages,
            status=status.HTTP_400_BAD_REQUEST
        )

    def path(self, request, pk):
        result = self.get_object(pk)
        serializer = ResultsDataSerializer(instance=result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer)
        return Response(
            serializer.error_messages,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        result = self.get_object(pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResultsDataViewSet(viewsets.ModelViewSet):
    queryset = ResultsData.objects.all()
    serializer_class = ResultsDataSerializer
