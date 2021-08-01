// import * as echarts from '{% static 'js/echarts.js' %}';


$(function () {
    // d3.select('#keshihua')
    //     .append('select')
    //     // .attr('name', 'lamb-select')
    //     .attr('id', 'lamb-select')
    // // .attr('onchange', lamb_change())
    // ;
    $('#lamb-select').change(function () {
        var select = $('#lamb-select').val();
        $.getJSON('/home/first_visual', {'limit': 'all', 'range': select}, function (data) {
            if (data['status'] === 200) {
                var dataset = [];
                data['data'].forEach(
                    function (i) {
                        dataset.push([i[0].replace('-', '/'), i[1]])
                    }
                );
                console.log(dataset);
                render(dataset);
            }
        })
    });

    // d3.select('#keshihua')
    //     .append('div')
    //     .attr('id', 'lamb')
    // ;
    $.getJSON('/home/count_year', function (data) {
        if (data['status'] === 200) {

            d3.select('#lamb-select')
                .selectAll('option')
                .data(data['year'])
                .enter()
                .append('option')
                .attr('value', function (d, i) {
                    return String(d);
                })
                .html(function (d) {
                    return String(d);
                })

        }
    })
    ;
    $.getJSON('/home/first_visual', {'limit': 'all', 'range': 'all'}, function (data) {
        if (data['status'] === 200) {
            var dataset = [];
            data['data'].forEach(
                function (i) {
                    dataset.push([i[0].replace('-', '/'), i[1]])
                }
            );
            render(dataset);
        }
    })
});

function lamb_change() {
    var select = document.getElementById('lamb-select');
    console.log(select);
    console.log(select.selectedIndex);
    console.log(select.value);
}

function render(dataset) {

    var chartDom = document.getElementById('lamb');
    var myChart = echarts.init(chartDom);
    var option;

    // var base = +new Date(1988, 9, 3);
    var oneDay = 24 * 3600 * 1000;
    var data = dataset;
    option = {
        tooltip: {
            trigger: 'axis',
            position: function (pt) {
                return [pt[0], '10%'];
            }
        },
        title: {
            left: 'center',
            text: '羔羊出生可视化',
        },
        toolbox: {
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            boundaryGap: false
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%']
        },
        dataZoom: [{
            type: 'inside',
            start: 0,
            end: 100
        }, {
            start: 0,
            end: 100
        }],
        series: [
            {
                name: '羔羊出生数量',
                type: 'line',
                smooth: true,
                symbol: 'none',
                areaStyle: {},
                data: data
            }
        ]
    };

    option && myChart.setOption(option);
}


