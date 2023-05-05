from django.shortcuts import render
from rest_framework import serializers
from django.core import serializers as s
from .models import Case, Item, Match
from rest_framework import viewsets
from rest_framework.decorators import api_view, schema
from rest_framework.decorators import action
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from django.forms.models import model_to_dict
from .compare import *


class CaseSerializer(serializers.ModelSerializer):
    versions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Case
        fields = ['id', 'case_name', 'short_circuit', 'blank_skip', 'create_time', 'update_time', 'versions']


# class VersionSerializer(serializers.ModelSerializer):
#     create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
#     update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
#
#     class Meta:
#         model = CaseVersion
#         fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class ItemMatchSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class CaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer

    def get_queryset(self):
        return Case.objects.all().order_by('-update_time')

    @action(detail=True)
    def get_fields(self, request, pk=None):
        _case = Case.objects.get(pk=pk)
        _fields = []
        for _item in _case.item_set.all().order_by('flag_index'):
            for _match in _item.matches.all().order_by('flag_index'):
                _fields.append({
                    'id': _match.id,
                    'description': _match.description,
                    'field': _match.field
                })
        return Response(_fields)


# class VersionViewSet(viewsets.ModelViewSet):
#     serializer_class = VersionSerializer
#     queryset = CaseVersion.objects.all().order_by('-update_time')
#     print('--------')
#     # def get_queryset(self):
#     #     return CaseVersion.objects.all().order_by('-update_time')


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all().order_by('-update_time')

    def list(self, request):
        queryset = Item.objects.filter(case=request.GET.get('case_id')).order_by('flag_index')
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = ItemMatchSerializer

    def get_queryset(self):
        return Match.objects.all().order_by('flag_index')

    def list(self, request):
        queryset = Match.objects.filter(rule=request.GET.get('rule_id')).order_by('flag_index')
        serializer = ItemMatchSerializer(queryset, many=True)
        return Response(serializer.data)


class RuleMatch(APIView):
    def get(self, request):
        _case_id = 5
        _fields = {"age": 20, 'nation': 'usa', 'weight': 50, 'interest': 2}
        _case = Case.objects.get(pk=_case_id)
        _list = []
        for _item in _case.item_set.all().order_by('flag_index'):
            _return_value = _item.return_value
            _match_result = {
                'rule_id': _item.id,
                'rule_name': _item.rule_name,
                'list': [],
                'min_match_amount': _item.min_match_amount
            }
            _match_count = 0
            for _match in _item.matches.all().order_by('flag_index'):
                if _match.field in _fields.keys():
                    if compare_map[_match.match_type](_fields[_match.field], model_to_dict(_match), _fields):
                        _match_result['list'].append({
                            _match.description: 1
                        })
                        _match_count += 1
                    else:
                        _match_result['list'].append({
                            _match.description: 2
                        })
                        _return_value = ''
                else:
                    if _case.blank_skip == 1:
                        _match_result['list'].append({
                            _match.description: 0
                        })
                    else:
                        _match_result['list'].append({
                            _match.description: 2
                        })
                        _return_value = ''
            if _item.min_match_amount == 0: #全匹配
                # 实际匹配数小于规则数
                if _match_count < _item.matches.count():
                    _return_value = ''
            #   实际匹配数小于要求匹配数，同时小于规则数
            elif _match_count < _item.min_match_amount and _match_count < _item.matches.count():
                _return_value = ''
            _match_result['match_count'] = _match_count
            _match_result['result'] = _return_value

            _list.append(_match_result)
            if _return_value != '':
                if _case.short_circuit == 1:
                    break
        return Response(_list)

    def post(self, request):
        _obj = json.loads(request.body)
        _case_id = _obj['case']
        _fields = _obj['fields']
        _case = Case.objects.get(pk=_case_id)
        for _item in _case.item_set.all().order_by('flag_index'):
            for _match in _item.matches.all().order_by('flag_index'):
                print(model_to_dict(_match))
        return Response(model_to_dict(_case))
