dataset = [
    {"key": '北京', "value": 1334}, {"key": '广东', "value": 997}, {"key": '上海', "value": 982}, {
        "key": '浙江',
        "value": 335
    }, {"key": '江苏', "value": 177}
];
console.log(dataset)
// dataset = [{'key': '南昌', 'house': 1.3103, 'salary': 42}, {'key': '杭州', 'house': 3.1581, 'salary': 38}, {
//     'key': '深圳',
//     'house': 7.1795,
//     'salary': 35
// }, {'key': '广州', 'house': 3.5537, 'salary': 32}, {'key': '北京', 'house': 6.8616, 'salary': 32}, {
//     'key': '厦门',
//     'house': 4.6655,
//     'salary': 32
// }, {'key': '武汉', 'house': 1.7158, 'salary': 30}, {'key': '成都', 'house': 1.6227, 'salary': 30}, {
//     'key': '贵阳',
//     'house': 0.9469,
//     'salary': 30
// }, {'key': '上海', 'house': 5.4732, 'salary': 29}]
// ;
div_id = 'keshihua1';
$(function () {
    $.getJSON('/home/first_visual',{'limit':20,'range':'all'},function (data) {
        console.log(data);
        if (data['status']===200) {
            dataset = [];
            data['data'].forEach(
                function (i) {
                    dataset.push({key:i[0],value:i[1]})
                }
            );
            console.log(1);
            console.log(dataset);
            render_zhu(dataset, div_id, 1000, 600, 150);
        }
    })
});

// render_zhu(dataset, div_id, 1000, 240, 40);

function render_zhu(dataset, select, w, h, margin) {
    var svg = d3.select('#' + select).append('svg')
        .attr('width', w)
        .attr('height', h)
    ;

    svg.append('text')
        .attr('class', 'title')
        .text('羔羊出生可视化')
        .attr('x', w / 2)
        .attr('y', margin * 2 / 3)
        .attr('fill', '#000')
        .attr('text-anchor', 'middle')
        .attr('font-size', '25px')
    ;

    x = [];
    for (i = 0; i < dataset.length; i++) {
        x.push(dataset[i].key);
    }
    var xscale = d3.scaleBand()
        .domain(x)
        .rangeRound([margin, w - margin])
        .paddingInner(0.25);


    var yscale = d3.scaleLinear()
    // .domain([0, d3.max(dataset, function (d) {
    //     return d.house;
    // })])
        .domain([0, 5])
        .range([h - margin, margin]);

    var xAxis = d3.axisBottom()
        .scale(xscale)
        .ticks(5)
        // .tickSize(5,5)
    ;
    var yAxis = d3.axisLeft()
        .scale(yscale)
    ;

    // var color = d3.scaleOrdinal(d3.schemeCategory20);


    var line = d3.line()
        .x(function (d) {
            return xscale(d.key);
        })
        .y(function (d) {
            return yscale(d.value);
        })
        .curve(d3.curveLinear)
    ;

    //生成折线的path
    var path_g = svg.append('g');
    path_g
        .append('path')
        .attr('class', 'draw-house')
        .attr('d', line(dataset))
        .attr('stroke', '#000')
        .attr('stroke-width', 3)
        .attr('fill', 'none')

    ;

    //生成文本
    var text_g = svg.append('g');
    text_g.selectAll('text')
        .data(dataset)
        .enter()
        .append('text')
        .text(function (d) {
            return d.value;
        })
        .attr('x', function (d) {
            return xscale(d.key);
        })
        .attr('y', function (d) {
            return yscale(d.value);
        })
        .attr('fill', '#000')
        .attr('text-anchor','middle')
        // .attr('transform', 'rotate(30)')
    ;



    var x_g = svg.append('g');
    x_g.attr('class', 'xaxis')
        .attr('color', '#000')
        .attr('transform', 'translate(0,' + (h - margin) + ')')
        .call(xAxis)
    ;
    svg.select('.xaxis')
        .selectAll('g')
        .selectAll('text')
        .attr('transform', 'matrix(0,1,-1,0,15,60)')
        // .attr('transform','translate(0,50)')
    ;
    var yaxis_g = svg.append('g');

    yaxis_g.attr('class', 'yaxis')
        .attr('transform', 'translate(' + margin + ',0)')
        .call(yAxis);

    first_xticks=svg.select('.xaxis')
        .select('g')
        .attr('transform')
    ;

    var x_shift=first_xticks.match(/translate\((.*),.*?\)/);
    path_g
        .attr('transform','translate('+(x_shift[1]-margin)+',0)')
    ;

    text_g
        .attr('transform','translate('+(x_shift[1]-margin)+',0)')



    d3.selectAll('.axis').selectAll('path')
        .attr('stroke', '#000');
    d3.selectAll('.axis').selectAll('line')
        .attr('stroke', '#000');
    d3.selectAll('.axis').selectAll('text')
        .attr('stroke', '#000')
        .attr('font-size', '12px')
        .attr('font-weight', 'normal')
    ;
}


