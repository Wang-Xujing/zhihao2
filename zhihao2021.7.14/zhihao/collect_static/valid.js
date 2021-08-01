// var $js=$('#django-admin-form-add-constants');
// const model_name=$js.data('model-name');

$(function () {

    var submit = $(":submit");
    console.log(submit);
    submit.each(function () {
        $(this).attr('onClick', 'return check()');
        console.log($(this))
    });

    monitor_live_num()

})
;

function monitor_live_num() {
    var field = 'live_num';
    var div_basic = $('.field-' + field);
    var $input = $("#id_" + field);
    if (typeof ($input.val()) == 'undefined') {
        return
    }
    $input.change(function () {
        var value = $input.val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
        console.log(value);
        if (value < 6) {
            console.log('ok');
            div_basic.children('ul').remove();
            $('.add-after').remove();

            for (var i = 1; i <= value; i++) {

                div_basic.after('<div class="form-row field-pre_num' + String(i) + ' add-after"><div><label for="id_pre_num' + String(i) + '">羔羊防疫耳号' + String(i) + '</label> <input type="text" name="pre_num' + String(i) + '" class="vTextField" id="id_pre_num' + String(i) + '" maxlength="16"></div></div>');

                div_basic.after('<div class="form-row field-bir_weight' + String(i) + ' add-after"><div><label for="id_bir_weight' + String(i) + '">羔羊出生重' + String(i) + '</label> <input type="number" name="bir_weight' + String(i) + '" id="id_bir_weight' + String(i) + '" ></div></div>');

                div_basic.after('<div class="form-row field-sex' + String(i) + '  add-after"><div><label for="id_sex' + String(i) + '">羔羊性别' + String(i) + '</label><select name="sex' + String(i) + '" id="id_sex' + String(i) + '"><option value="" selected="">---------</option><option value="1">母</option><option value="0">公</option></select>');

                div_basic.after('<div class="form-row field-color' + String(i) + '"><div><label for="id_color' + String(i) + '">羔羊毛色' + String(i) + ':</label><select name="color' + String(i) + '" id="id_color' + String(i) + '"><option value="" selected="">---------</option><option value="0">白</option><option value="1">黑</option><option value="2">咖</option><option value="3">混合色</option></select>');

                div_basic.after('<div class="form-row field-rank' + String(i) + '"><div><label for="id_rank' + String(i) + '">羔羊等级' + String(i) + ':</label><select name="rank' + String(i) + '" id="id_rank' + String(i) + '"><option value="" selected="">---------</option><option value="0">特级</option><option value="1">一级</option><option value="2">二级</option><option value="3">三级</option><option value="9">未评级</option></select>');

                div_basic.after('<div>羔羊 '+String(i)+'</div>')
            }
        } else {
            $ul = div_basic.children('ul');
            if ($ul.length === 0) {
                div_basic.prepend('<ul class="errorlist"><li>最多是5个</li></ul>');
            }
        }
    })
}

function finnal_check_allSelect_field(model_name) {

    var $select = $("select");
    map_select = {
        'breedinginfo': 'select[id*=\'breeding\']'
    }
    if (model_name === 'breedinginfo') {
        $select = $("select[id*='breeding']");
    }
    var state = true;
    console.log($select);
    $select.each(function () {
        var div = $(this).parent().parent();

        var value = $(this).val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
        if (value) {
            console.log('ok');
            div.children('ul').remove();
        } else {
            $ul = div.children('ul');
            if ($ul.length === 0) {
                div.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
            }
            state = false
        }
    });
    return state
}

function check_allSelect_field() {

    var $select = $("select");
    $select.each(function () {
        var div = $(this).parent().parent();
        $(this).change(function () {
            var value = $(this).val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
            if (value) {
                console.log('ok');
                div.children('ul').remove()
            } else {
                $ul = div.children('ul');
                if ($ul.length === 0) {
                    div.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
                }

            }
        })
    })

}

function finnal_check_out_field(field, input_name) {
    var div_basic = $('.field-' + field);
    var $basicBasicinfo = $("#" + input_name);
    console.log(div_basic);

    if (typeof ($basicBasicinfo.val()) == 'undefined' || div_basic.length === 0) {
        return true
    }
    var value = $basicBasicinfo.val().trim();  //val函数取输入框中的值  trim函数去除边缘空格

    console.log(value);
    var pat = /已经选择/;
    if (value) {
        console.log('ok');
        div_basic.children('ul').remove();
        return true
    } else {
        $ul = div_basic.children('ul');
        if ($ul.length === 0) {
            div_basic.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
        }
        return false
    }
    // var pat = /已经选择/;
    // if (pat.test(value)) {
    //     console.log('ok');
    //     div_basic.children('ul').remove();
    //     return true
    // } else {
    //     $ul = div_basic.children('ul');
    //     if ($ul.length === 0) {
    //         div_basic.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
    //     }
    //     return false
    // }

}

function check_out_field(field, input_name) {
    var div_basic = $('.field-' + field);
    var $basicBasicinfo = $("#" + input_name);
    if (typeof ($basicBasicinfo.val()) == 'undefined') {
        return true
    }
    $basicBasicinfo.change(function () {
        var value = $basicBasicinfo.val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
        console.log(value);
        var pat = /已经选择/;
        if (pat.test(value)) {
            console.log('ok');
            div_basic.children('ul').remove()
        } else {
            $ul = div_basic.children('ul');
            if ($ul.length === 0) {
                div_basic.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
            }
        }
    })
}

function check_input_field(fields) {
    for (var i = 0; i < fields.length(); i++) {
        var field = fields[i];
        var div_basic = $('.field-' + field);
        var $basicBasicinfo = $("#id_" + field);
        if (typeof ($basicBasicinfo.val()) == 'undefined') {
            continue
        }
        $basicBasicinfo.change(function () {
            var value = $basicBasicinfo.val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
            console.log(value);
            if (value) {
                console.log('ok');
                div_basic.children('ul').remove()
            } else {
                $ul = div_basic.children('ul');
                if ($ul.length === 0) {
                    div_basic.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
                }
            }
        })
    }

}

function final_check_input_field(fields) {
    var a = true;
    for (var i = 0; i < fields.length; i++) {
        var field = fields[i];
        var div_basic = $('.field-' + field);
        var $basicBasicinfo = $("#id_" + field);
        if (typeof ($basicBasicinfo.val()) == 'undefined') {
            console.log('o no');
            continue
        }
        var value = $basicBasicinfo.val().trim();  //val函数取输入框中的值  trim函数去除边缘空格
        if (value) {
            div_basic.children('ul').remove();
        } else {
            $ul = div_basic.children('ul');
            if ($ul.length === 0) {
                div_basic.prepend('<ul class="errorlist"><li>这个字段是必填项。</li></ul>');
            }
            a = false
        }
    }
    return a

}

//控制表单是否提交
function check() {
    // var $js = $('#django-admin-form-add-constants');
    // const model_name = $js.data('model-name');
    var $js = $('form');
    var model_name = $js.attr('id');
    if (model_name) {
        model_name = model_name.slice(0, -5)
    }
    var a = true;
    //检验基本羊添加
    a = finnal_check_out_field('basic_id', 'basic_basicinfo') && a;
    console.log(a);
    //配种信息里的公母羊添加
    a = finnal_check_out_field('ewe_id', 'e_breed_rutinfo') && a;
    console.log(a);
    a = finnal_check_out_field('ram_id', 'basic_basicinfo_ram') && a;
    console.log(a);
    //羊羔添加
    a = finnal_check_out_field('lamb_id', 'e_breed_lambinfo') && a;
    console.log(a);
    //圈舍
    a = finnal_check_out_field('hurdle_id', 'colony_houseinfo') && a;
    console.log(a);
    a = finnal_check_out_field('house_id', 'colony_houseinfo') && a;
    console.log(a);
    //配种信息添加
    a = finnal_check_out_field('breeding_id', 'e_breed_breedinginfo') && a;
    console.log(a);
    //疫苗药品厂家
    a = finnal_check_out_field('vaccine_id', 'supply_commodityinfo') && a;
    console.log(a);
    a = finnal_check_out_field('maker_id', 'supply_v_suppliersinfo') && a;
    console.log(a);
    a = finnal_check_out_field('maker_id', 'supply_f_suppliersinfo') && a;
    console.log(a);
    a = finnal_check_out_field('vac_maker', 'supply_v_suppliersinfo') && a;
    console.log(a);
    a = finnal_check_out_field('drug_id', 'supply_commodityinfo') && a;
    console.log(a);

    //原产地名
    a = finnal_check_out_field('manu_info_id', 'basic_manuinfo') && a;
    console.log(a);

    //所有的下拉选择
    const model_array = ['breederconditioninfo', 'cutinfo', 'quarantineinfo', 'nursinginfo'];
    if (!model_array.includes(model_name)) {
        a = finnal_check_allSelect_field(model_name) && a;
        console.log(a);
    }

    //检验其他字段
    const valid_fields = {
        'postnatalinfo': ['live_num', 'delivery_date'],//产后信息
        'artificialfeedinginfo': ['delivery_date', 'feeding_staff'],//人工喂养
        'semencollectinfo': ['E_date'],//采精
        'breedinginfo': ['breeding_date'],//配种
        'pregnantinfo': ['check_type'],//
        'weaninginfo': ['Delivery_date'],
        'lambinfo': ['ele_num', 'pre_num', 'f_ele_num', 'f_pre_num', 'm_ele_num', 'm_pre_num'],
        'g_salesinfo': ['sales_order', 'billing_unit', 'name', 'buyer', 'buyer_phone', 'sales_site'],
        'slaughtersegmentinfo': ['source'],
        'binformationinfo': ['date', 'source'],
        'vaccine_in': ['v_name', 'produce_date', 'expiration_date', 'produce_num', 'in_amount', 'unit_price', 'in_time', 'f_date'],
        'vaccine_out': ['outbound_no', 'v_name', 'out_purposes', 'out_staff', 'contact_phone', 'num'],
        'feedingin': ['f_name', 'buy_time', 'billing_unit', 'quantity', 'unit_price', 'purpose', 'f_date'],
        'feeding_out': ['outbound_no', 'f_name', 'out_purposes', 'out_staff', 'contact_phone', 'num'],
        'breederconditioninfo': ['mon_age', 'color', 'rank'],
        'cutinfo': ['cut_time', 'rank', 'color'],
        'v_suppliersinfo': ['supplier_name', 'address', 'f_date', 'operation'],
        ['feedhouseinfo']: ['date', 'quantity']


    };
    console.log(model_name);
    if (model_name in valid_fields) {
        a = final_check_input_field(valid_fields[model_name]) && a;
        console.log(a);
    }


    if (a === false) {
        $('html, body').animate({scrollTop: 0}, 'slow');
    }
    return a;
}