/**
 *
 * Active Charts using Highcharts demonstration
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 * 
 * Copyright 2012, Script Tutorials
 * http://www.script-tutorials.com/
 */

// Change Chart type function
// function ChangeChartType(chart, series, newType) {
//     newType = newType.toLowerCase();
//     for (var i = 0; i < series.length; i++) {
//         var srs = series[0];
//         try {
//             srs.chart.addSeries({
//                     type: newType,
//                     stack: srs.stack,
//                     yaxis: srs.yaxis,
//                     name: srs.name,
//                     color: srs.color,
//                     data: srs.options.data
//                 },
//                 false);
//             series[0].remove();
//         } catch (e) {}
//     }
// }

// Two charts definition
var chart1, chart2;

// Once DOM (document) is finished loading

$(document).ready(function() {

    $.ajax({
        url: "http://127.0.0.1:8000/",
        dataType: "JSON",
        type: "GET",
        async: "false",
        data: {},
        success: function(data) {

            var data1 = data['data'][0]
            var data2 = data['data'][1]
            var data3 = data['data'][2]
            var data4 = data['data'][3]
            var data5 = data['data'][4]
            var data6 = data['data'][5]
            var data7 = data['data'][6]
            var data8 = data['data'][7]
            console.log(data1)
            console.log(data2)
            console.log(data3)
            console.log(data4)
            console.log(data5)
            console.log(data6)
            console.log(data7)
            console.log(data8)
            var fb1 = data1[4]
            var zjl1 = data1[1]
            var pjsd1 = data1[2]
            var zgsd1 = data1[3]
            var fb2 = data2[4]
            var zjl2 = data2[1]
            var pjsd2 = data2[2]
            var zgsd2 = data2[3]
            var fb3 = data3[4]
            var zjl3 = data3[1]
            var pjsd3 = data3[2]
            var zgsd3 = data3[3]
            var fb4 = data4[4]
            var zjl4 = data4[1]
            var pjsd4 = data4[2]
            var zgsd4 = data4[3]
            var fb5 = data5[4]
            var zjl5 = data5[1]
            var pjsd5 = data5[2]
            var zgsd5 = data5[3]
            var fb6 = data6[4]
            var zjl6 = data6[1]
            var pjsd6 = data6[2]
            var zgsd6 = data6[3]
            var fb7 = data7[4]
            var zjl7 = data7[1]
            var pjsd7 = data7[2]
            var zgsd7 = data7[3]
            var fb8 = data8[4]
            var zjl8 = data8[1]
            var pjsd8 = data8[2]
            var zgsd8 = data8[3]



            $("#1_a1_zjl").html(zjl1[0]);
            $("#1_a2_zjl").html(zjl1[1]);
            $("#1_b1_zjl").html(zjl1[2]);
            $("#1_b2_zjl").html(zjl1[3]);
            $("#1_a1_pjsd").html(pjsd1[0]);
            $("#1_a2_pjsd").html(pjsd1[1]);
            $("#1_b1_pjsd").html(pjsd1[2]);
            $("#1_b2_pjsd").html(pjsd1[3]);
            $("#1_a1_zgsd").html(zgsd1[0]);
            $("#1_a2_zgsd").html(zgsd1[1]);
            $("#1_b1_zgsd").html(zgsd1[2]);
            $("#1_b2_zgsd").html(zgsd1[3]);

            $("#2_a1_zjl").html(zjl2[0]);
            $("#2_a2_zjl").html(zjl2[1]);
            $("#2_b1_zjl").html(zjl2[2]);
            $("#2_b2_zjl").html(zjl2[3]);
            $("#2_a1_pjsd").html(pjsd2[0]);
            $("#2_a2_pjsd").html(pjsd2[1]);
            $("#2_b1_pjsd").html(pjsd2[2]);
            $("#2_b2_pjsd").html(pjsd2[3]);
            $("#2_a1_zgsd").html(zgsd2[0]);
            $("#2_a2_zgsd").html(zgsd2[1]);
            $("#2_b1_zgsd").html(zgsd2[2]);
            $("#2_b2_zgsd").html(zgsd2[3]);

            $("#3_a1_zjl").html(zjl3[0]);
            $("#3_a2_zjl").html(zjl3[1]);
            $("#3_b1_zjl").html(zjl3[2]);
            $("#3_b2_zjl").html(zjl3[3]);
            $("#3_a1_pjsd").html(pjsd3[0]);
            $("#3_a2_pjsd").html(pjsd3[1]);
            $("#3_b1_pjsd").html(pjsd3[2]);
            $("#3_b2_pjsd").html(pjsd3[3]);
            $("#3_a1_zgsd").html(zgsd3[0]);
            $("#3_a2_zgsd").html(zgsd3[1]);
            $("#3_b1_zgsd").html(zgsd3[2]);
            $("#3_b2_zgsd").html(zgsd3[3]);

            $("#4_a1_zjl").html(zjl4[0]);
            $("#4_a2_zjl").html(zjl4[1]);
            $("#4_b1_zjl").html(zjl4[2]);
            $("#4_b2_zjl").html(zjl4[3]);
            $("#4_a1_pjsd").html(pjsd4[0]);
            $("#4_a2_pjsd").html(pjsd4[1]);
            $("#4_b1_pjsd").html(pjsd4[2]);
            $("#4_b2_pjsd").html(pjsd4[3]);
            $("#4_a1_zgsd").html(zgsd4[0]);
            $("#4_a2_zgsd").html(zgsd4[1]);
            $("#4_b1_zgsd").html(zgsd4[2]);
            $("#4_b2_zgsd").html(zgsd4[3]);

            $("#5_a1_zjl").html(zjl5[0]);
            $("#5_a2_zjl").html(zjl5[1]);
            $("#5_b1_zjl").html(zjl5[2]);
            $("#5_b2_zjl").html(zjl5[3]);
            $("#5_a1_pjsd").html(pjsd5[0]);
            $("#5_a2_pjsd").html(pjsd5[1]);
            $("#5_b1_pjsd").html(pjsd5[2]);
            $("#5_b2_pjsd").html(pjsd5[3]);
            $("#5_a1_zgsd").html(zgsd5[0]);
            $("#5_a2_zgsd").html(zgsd5[1]);
            $("#5_b1_zgsd").html(zgsd5[2]);
            $("#5_b2_zgsd").html(zgsd5[3]);

            $("#6_a1_zjl").html(zjl6[0]);
            $("#6_a2_zjl").html(zjl6[1]);
            $("#6_b1_zjl").html(zjl6[2]);
            $("#6_b2_zjl").html(zjl6[3]);
            $("#6_a1_pjsd").html(pjsd6[0]);
            $("#6_a2_pjsd").html(pjsd6[1]);
            $("#6_b1_pjsd").html(pjsd6[2]);
            $("#6_b2_pjsd").html(pjsd6[3]);
            $("#6_a1_zgsd").html(zgsd6[0]);
            $("#6_a2_zgsd").html(zgsd6[1]);
            $("#6_b1_zgsd").html(zgsd6[2]);
            $("#6_b2_zgsd").html(zgsd6[3]);

            $("#7_a1_zjl").html(zjl7[0]);
            $("#7_a2_zjl").html(zjl7[1]);
            $("#7_b1_zjl").html(zjl7[2]);
            $("#7_b2_zjl").html(zjl7[3]);
            $("#7_a1_pjsd").html(pjsd7[0]);
            $("#7_a2_pjsd").html(pjsd7[1]);
            $("#7_b1_pjsd").html(pjsd7[2]);
            $("#7_b2_pjsd").html(pjsd7[3]);
            $("#7_a1_zgsd").html(zgsd7[0]);
            $("#7_a2_zgsd").html(zgsd7[1]);
            $("#7_b1_zgsd").html(zgsd7[2]);
            $("#7_b2_zgsd").html(zgsd7[3]);

            $("#8_a1_zjl").html(zjl8[0]);
            $("#8_a2_zjl").html(zjl8[1]);
            $("#8_b1_zjl").html(zjl8[2]);
            $("#8_b2_zjl").html(zjl8[3]);
            $("#8_a1_pjsd").html(pjsd8[0]);
            $("#8_a2_pjsd").html(pjsd8[1]);
            $("#8_b1_pjsd").html(pjsd8[2]);
            $("#8_b2_pjsd").html(pjsd8[3]);
            $("#8_a1_zgsd").html(zgsd8[0]);
            $("#8_a2_zgsd").html(zgsd8[1]);
            $("#8_b1_zgsd").html(zgsd8[2]);
            $("#8_b2_zgsd").html(zgsd8[3]);

            chart1 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_1',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb1
            });
            chart2 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_2',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb2
            });
            chart3 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_3',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb3
            });
            chart4 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_4',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb4
            });
            chart5 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_5',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb5
            });
            chart6 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_6',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb6
            });
            chart7 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_7',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb7
            });
            chart8 = new Highcharts.Chart({
                chart: {
                    renderTo: 'chart_8',
                    type: 'column',
                    height: 350,
                },
                title: {
                    text: '三十分钟速度分布'
                },
                xAxis: {
                    categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
                },
                yAxis: {
                    title: {
                        text: ''
                    }
                },
                series: fb8
            });

        },
        error: function() { console.log('2') }
    });

    // First chart initialization
    // chart1 = new Highcharts.Chart({
    //     chart: {
    //         renderTo: 'chart_1',
    //         type: 'column',
    //         height: 350,
    //     },
    //     title: {
    //         text: '三十分钟速度分布'
    //     },
    //     xAxis: {
    //         categories: ['0~1(m/s)', '1~2(m/s)', '2~3(m/s)', '3~4(m/s)', '4~5(m/s)', '>5(m/s)']
    //     },
    //     yAxis: {
    //         title: {
    //             text: ''
    //         }
    //     },
    //     series: [{
    //         name: 'a1',
    //         data: [5, 10, 20, 22, 25, 28]
    //     }, {
    //         name: 'a2',
    //         data: [15, 15, 18, 40, 30, 25]
    //     }, {
    //         name: 'b1',
    //         data: [1, 3, 6, 0, 50, 25]
    //     }, {
    //         name: 'b2',
    //         data: [1, 3, 6, 0, 50, 25]
    //     }]
    // });

    // $('.switcher').click(function() {
    //     var newType = $(this).attr('id');
    //     ChangeChartType(chart1, chart1.series, newType);
    // });
});