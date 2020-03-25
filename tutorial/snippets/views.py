import time

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        print(type(serializer.data), serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def inventory_list(request):
    """
    :param request:
    :return:
    """
    if request.method == "GET":
        res = [
            {
                "name": "Logstash",
                "code": "0002",
                "msg": "YES"
            },
        ]

        return Response(res)


@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk):

    if request.method == 'GET':
        res = {
            "name": "Logstash",
            "code": "0002"
        }

        return Response(res)


@api_view(['GET', 'POST'])
def order_list(request):

    time.sleep(10)
    try:
        a = ' ' * 1000 * 1000 * 100
        print(a)
    except KeyboardInterrupt:
        print("Will release the memory.")

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def user_list(request):

    time.sleep(40)

    res = [
        {
            "id": "001",
            "username": "zhangsan",
        },
        {
            "id": "002",
            "username": "lisi"
        }
    ]

    return Response(res)
