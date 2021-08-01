from django.db import models
from django.utils import timezone
from apps.colony.models import HouseInfo
# Create your models here.
# 饲喂管理系统表

class feedingInfo(models.Model):
    

    fodder_choices = ((0, '全株青贮料'), (1, '黄贮料'), (2, '花生秧'), (3, '豆秸'), (4, '玉米秸秆'), (5, '苜蓿'),
                      (6, '羊草'), (7, '大蒜皮'), (8, '豆腐渣'), (9, '淀粉渣'), (10, '玉米皮'), (11, '黄豆荚'),
                      (12, '酒糟'), (13, '麦秸'), (14, '麦糠'), (15, '葵花籽皮'), (16, '花生壳'))
    fodder = models.IntegerField(verbose_name="草料", choices=fodder_choices)

    concentrate_choices = ((1, '玉米'), (2, '大麦'), (3, '小麦麸'), (4, '米糠'), (5, '大豆粕'), (6, '膨化大豆'), (7, '花生饼'),
                           (8, '全棉籽'), (9, '棉籽粕'), (10, '棉仁粕'), (11, 'DDGS'), (12, '葵花籽粕'), (13, '葵花仁粕'), (14, '菜粕'),
                           (15, '玉米胚芽粕'), (16, '羔羊开口料'), (17, '羔羊颗粒料'), (18, '精补料'), (19, '浓缩料(28%蛋白)'),
                           (20, '浓缩料(30%蛋白)'), (21, '浓缩料(32%蛋白)'), (22, '预混料(钙磷含量填写)'), (23, '发酵料'), (24, '小苏打'), (25, '盐'))
    concentrate = models.IntegerField(verbose_name="精料", choices=concentrate_choices)

    category_choices = ((1, '育肥羊'), (2, '育成羊'), (3, '种公羊'), (4, '繁殖母羊'))
    category = models.IntegerField(verbose_name="品种", choices=category_choices)

    variety_choices = ((1, '寒羊串'), (2, '太行山羊'), (3, '承德无角黑山羊'), (4, '绒山羊'), (5, '波尔山羊'), (6, '德克赛尔'), (7, '东弗里升'),
                       (8, '澳洲白'), (9, '夏洛莱'), (10, '杜波'), (11, '无角道赛特'), (12, '萨福克'), (13, '湖羊'), (14, '小尾寒羊'),
                       (15, '奶山羊串'), (16, '波尔串'), (17, '湖羊串'), (18, '杜波串'), (19, '细杂羊'))
    variety = models.IntegerField(verbose_name="品类", choices=variety_choices)

    sex_choices = ((0, '母'), (1, '公'))
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices)

    growing = models.CharField(verbose_name="生长期", max_length=15)
    n_diagnosis = models.BooleanField(verbose_name="营养诊断")
    n_requirements = models.TextField(verbose_name="营养需求")
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        verbose_name = '饲喂管理表'
        verbose_name_plural = '饲喂管理表'


class feedHouseInfo(models.Model):
    house_id=models.IntegerField(verbose_name='圈舍号')

    date=models.DateField(verbose_name='喂养日期',blank=True)
    staff=models.CharField(verbose_name='喂养人员', blank=True, max_length=8)
    billing_unit = models.CharField(verbose_name="重量单位", max_length=3, default="kg",blank=True,null=True)
    quantity = models.FloatField(verbose_name="重量",blank=True,null=True)
    fodder_choices = ((0, '全株青贮料'), (1, '黄贮料'), (2, '花生秧'), (3, '豆秸'), (4, '玉米秸秆'), (5, '苜蓿'),
                      (6, '羊草'), (7, '大蒜皮'), (8, '豆腐渣'), (9, '淀粉渣'), (10, '玉米皮'), (11, '黄豆荚'),
                      (12, '酒糟'), (13, '麦秸'), (14, '麦糠'), (15, '葵花籽皮'), (16, '花生壳'))
    fodder = models.IntegerField(verbose_name="草料", choices=fodder_choices,blank=True,null=True)

    concentrate_choices = ((1, '玉米'), (2, '大麦'), (3, '小麦麸'), (4, '米糠'), (5, '大豆粕'), (6, '膨化大豆'), (7, '花生饼'),
                           (8, '全棉籽'), (9, '棉籽粕'), (10, '棉仁粕'), (11, 'DDGS'), (12, '葵花籽粕'), (13, '葵花仁粕'), (14, '菜粕'),
                           (15, '玉米胚芽粕'), (16, '羔羊开口料'), (17, '羔羊颗粒料'), (18, '精补料'), (19, '浓缩料(28%蛋白)'),
                           (20, '浓缩料(30%蛋白)'), (21, '浓缩料(32%蛋白)'), (22, '预混料(钙磷含量填写)'), (23, '发酵料'), (24, '小苏打'),
                           (25, '盐'))
    concentrate = models.IntegerField(verbose_name="精料", choices=concentrate_choices,blank=True,null=True)

    category_choices = ((1, '育肥羊'), (2, '育成羊'), (3, '种公羊'), (4, '繁殖母羊'))
    category = models.IntegerField(verbose_name="品种", choices=category_choices,blank=True,null=True)

    variety_choices = ((1, '寒羊串'), (2, '太行山羊'), (3, '承德无角黑山羊'), (4, '绒山羊'), (5, '波尔山羊'), (6, '德克赛尔'), (7, '东弗里升'),
                       (8, '澳洲白'), (9, '夏洛莱'), (10, '杜波'), (11, '无角道赛特'), (12, '萨福克'), (13, '湖羊'), (14, '小尾寒羊'),
                       (15, '奶山羊串'), (16, '波尔串'), (17, '湖羊串'), (18, '杜波串'), (19, '细杂羊'))
    variety = models.IntegerField(verbose_name="品类", choices=variety_choices,blank=True,null=True)

    sex_choices = ((0, '母'), (1, '公'))
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices,blank=True,null=True)

    growing = models.CharField(verbose_name="生长期", max_length=15,blank=True,null=True)
    n_diagnosis = models.BooleanField(verbose_name="营养诊断",blank=True,null=True)
    n_requirements = models.TextField(verbose_name="营养需求",blank=True,null=True)
    notes=models.TextField(verbose_name='备注',max_length=200,blank=True,null=True)
    belong = models.IntegerField(verbose_name='羊场域')
    def house(self):
        pid = HouseInfo.objects.filter(id=self.house_id).values("pid").first()['pid']
        if pid!=0:
            house = HouseInfo.objects.filter(id=pid).values("name").first()['name']+'-' + HouseInfo.objects.filter(id=self.house_id).values("name").first()['name']
        else:
            house = HouseInfo.objects.filter(id=self.house_id).values("name").first()['name']
        return house
    class Meta:
        verbose_name_plural='圈舍喂养信息'
