from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from apps.basic.models import BasicInfo
from apps.basic.models import BreederconditionInfo
from apps.e_breed.models import breedingInfo
from apps.e_breed.models import postnatalInfo,LambInfo
import copy
class xipu(View):
    def check_choices(self,models):
        data={}
        for i in models:
            fields=i._meta.fields
            for j in fields:
                if j.choices:
                    data[j.name]=dict(j.choices)
        return data
    def get_basic(self,basic_id):
        basic=BasicInfo.objects.filter(id=basic_id).first()
        if basic:
            variety_choices=dict(BasicInfo.variety_choices)
            rank_choice=dict(BasicInfo.rank_choice)
            sex_choices=dict(BasicInfo.sex_choices)
            lamb_self=LambInfo.objects.filter(basic_id=basic_id).first()
            together_num=''
            if lamb_self:
                breed_id=lamb_self.breeding_id
                postna=postnatalInfo.objects.filter(breeding_id=breed_id).first()
                if postna:
                    together_num=postna.live_num
            dict_1={
                'variety':variety_choices[basic.variety],
                'pre_num':basic.pre_num,
                'ele_num':basic.ele_num,
                'sex':sex_choices[basic.sex],
                'birth':basic.birth,
                'rank':rank_choice.get(basic.rank),
                'bir_weight':basic.bir_weight,
                'wea_weight':basic.wea_weight,
                'manu_info_name':basic.manu_info_name,
                'together_num':together_num
            }
            for i in dict_1.keys():
                if dict_1[i]==None:
                    dict_1[i]=''
            return dict_1
    def get_first_table(self,basic_id):
        first=BreederconditionInfo.objects.filter(basic_id=basic_id)
        if first:
            list=[]
            mon_age_choice=dict(BreederconditionInfo.mon_age_choice)
            rank_choice = dict(BreederconditionInfo.rank_choice)
            for i in first:
                dict_1={
                    'mon_age':mon_age_choice[i.mon_age],
                    'rank':rank_choice[i.rank],
                    'other':i
                }
                list.append(dict_1)
                print(dict_1)
            return list
    def get_second_table(self,basic_id):
        basic=BasicInfo.objects.filter(id=basic_id).first()
        if basic==None:
            return None
        father=BasicInfo.objects.filter(id=basic.father_id).first()
        mother = BasicInfo.objects.filter(id=basic.mother_id).first()
        familiy_list=[
            (basic.father_id ,'父亲') if basic else '',
            (basic.mother_id,'母亲') if basic else '',
            (father.father_id,'祖父') if father else '',
            (father.mother_id,'祖母') if father else '',
            (mother.father_id,'外祖父') if mother else '',
            (mother.mother_id,'外祖母') if mother else '',
        ]
        data=[]
        rank_choices=dict(BreederconditionInfo.rank_choice)
        for one in familiy_list:
            if one!='':
                id,name=one
            # if id !='无':
                this_basic=BasicInfo.objects.filter(id=id).first()
                this_other=BreederconditionInfo.objects.filter(basic_id=id).first()
                dict_1={
                    'name':name,
                    'ele_num':this_basic.ele_num if this_basic else '',
                    'pre_num': this_basic.pre_num if this_basic else '',
                    'rank':rank_choices[this_other.rank] if this_other else '',
                    'other':this_other if this_other else ''
                }
                data.append(dict_1)
        return data
    def get_third_table(self,basic_id):
        basic=BasicInfo.objects.filter(id=basic_id).first()
        if basic:
            sex=basic.sex
            if sex==0:
                breeding=breedingInfo.objects.filter(ewe_id=basic_id)
            else:
                breeding=breedingInfo.objects.filter(ram_id=basic_id)

            data=[]
            for i in breeding:
                friend=BasicInfo.objects.filter(id=i.ewe_id if sex==0 else i.ram_id).first()
                breed_id=i.id
                postnatal=postnatalInfo.objects.filter(breeding_id=breed_id).first()
                lambs=LambInfo.objects.filter(breeding_id=breed_id)
                dict_init={
                    'breeding_date':i.breeding_date,
                    'friend_ele_num':friend.ele_num,
                    'delivery_date':postnatal.delivery_date,
                    'live_num':postnatal.live_num,
                }
                for j in lambs:
                    dict_one=copy.deepcopy(dict_init)
                    dict_one['other']=j
                    data.append(dict_one)
            return data
    def get(self,request):
        id=request.GET.get('id')
        context={}
        if id:
            context['basic']=self.get_basic(int(id))
            context['first'] = self.get_first_table(int(id))
            context['second'] = self.get_second_table(int(id))
            context['third'] = self.get_third_table(int(id))
        return render(request,'home/xipu.html',context=context)