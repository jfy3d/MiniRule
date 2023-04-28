from django.db import models


class Case(models.Model):
    case_name = models.CharField("规则方案", max_length=100)
    short_circuit = models.SmallIntegerField('短路', default=0)
    blank_skip = models.SmallIntegerField('空值跳过', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.case_name


# class CaseVersion(models.Model):
#     version_name = models.CharField("版本名称", max_length=100)
#     version_code = models.IntegerField('版本号')
#     version_default = models.BooleanField('默认版本')
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now_add=True)
#     case = models.ForeignKey(Case, related_name='versions', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.version_name


class Item(models.Model):
    rule_name = models.CharField("规则名称", max_length=100)
    return_value = models.CharField('返回值', max_length=200)
    # min_match_amount 0 全部匹配
    min_match_amount = models.IntegerField('最少匹配数', default=0)
    flag_index = models.IntegerField('排序号', default=0)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.rule_name


class Match(models.Model):
    field = models.CharField("字段", max_length=100)
    description = models.CharField('描述', max_length=200)
    match_type = models.CharField('描述', max_length=20)
    target_type = models.CharField('目标比对类型', max_length=20)
    target_value = models.CharField('目标值', max_length=200)
    flag_index = models.IntegerField('排序号', default=0)
    rule = models.ForeignKey(Item, related_name='matches', on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.description


