from rest_framework import viewsets
from .serializers import DocumentSerializer, SearchSerializer
from .models import Document
from rest_framework.views import APIView
from django.db.models import Q, query
from rest_framework.response import Response




class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class SearchView(APIView):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('search', '')
        document = Document.objects.all()
        if query:
            document = document.filter(Q(id__icontains=query) | Q(text__icontains=query))
            context = {'request': request}
            return Response({'document': SearchSerializer(document, context=context, many=True).data,})
        return Response()
