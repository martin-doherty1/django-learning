# search/views.py

import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q, Search, A
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from blog.documents import ArticleDocument, UserDocument, CategoryDocument
from blog.serializers import ArticleSerializer, UserSerializer, CategorySerializer

from gym.serializers import ExerciseSerializer, AggregationSerializer
from gym.documents import ExerciseDocument


class PaginatedElasticSearchAggAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def get_agg_expression(self):
        """This method should be overridden
                and return a Q() expression."""

    def get(self, request):
        try:
            agg = self.get_agg_expression()
            search = Search(index="exercises")
            search.aggs.bucket("type_term", agg)
            response = search.execute()

            agg_results = []
            for bucket in response.aggregations.type_term.buckets:
                result = {
                    "key": bucket.key,
                    "doc_count": bucket.doc_count
                }
                agg_results.append(result)

            results = self.paginate_queryset(agg_results, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class PaginatedElasticSearchQueryAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            http_response = self.get_paginated_response(serializer.data)
            return http_response
        except Exception as e:
            return HttpResponse(e, status=500)


# views


class SearchUsers(PaginatedElasticSearchQueryAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q("bool",
                 should=[
                     Q("match", username=query),
                     Q("match", first_name=query),
                     Q("match", last_name=query),
                 ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchQueryAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    def generate_q_expression(self, query):
        return Q(
            "multi_match", query=query,
            fields=[
                "name",
                "description",
            ], fuzziness="auto")


class SearchArticles(PaginatedElasticSearchQueryAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q(
            "multi_match", query=query,
            fields=[
                "title",
                "author",
                "type",
                "content"
            ], fuzziness="auto")


class SearchExercises(PaginatedElasticSearchQueryAPIView):
    serializer_class = ExerciseSerializer
    document_class = ExerciseDocument

    def generate_q_expression(self, query):
        return Q("multi_match", query=query,
                 fields=[
                     "exercise_name^2",
                     "body_part",
                     "description",
                     "type"
                 ], fuzziness="auto")


class GetNumberOfTypes(PaginatedElasticSearchAggAPIView):
    serializer_class = AggregationSerializer
    document_class = ExerciseDocument

    def get_agg_expression(self):
        return A('terms', field="type")
