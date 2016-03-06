function drawGraph(){
        $('#image-container').css('position', 'fixed')
        $('#image-container').remove();
        
        $('#graph').fadeIn()
        
    $('#graph').highcharts({
        title: {
            text: 'Average Mood',
            x: -20 //center
        },
        subtitle: {
            text: 'Source: Twitter.com',
            x: -20
        },
        xAxis: {
            categories: ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            title: {
                text: 'Mood'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: user,
            data: [1, 1, 0, 0, -1, -1, -1]
        }]
    });
    
}


function pieChart(){
    $('#graph').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Mood Break-Down'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'Positive',
                y: 50,
                sliced: true,
                selected: true
            }, {
                name: 'Negative',
                y: 25,
            }, {
                name: 'Neutral',
                y: 25
            }]
        }]
    });
}

$(document).ready(function(){
    user = "";
    
    $('#search').bind('keypress keydown', function(e){
       if(e.keyCode == 13) { e.preventDefault(); }
    });
    
    
    
    $("input[type=text]").keyup(function(e){
        if(e.keyCode == '13'){
            user = $("#user_name").val();
            drawGraph();
        }
        $(".jumbotron > .container > row > .col-md-4 > form").css("animation-play-state", "running");
        $(".jumbotron > .container > row > .col-md-4 > img").css({"animation-duration":"2s","animation-name":"query_user_img","animation-direction":"forward","animation-iteration-count":"1","animation-fill-mode":"forward"});

    });
    
    
    $("#submit").click(function(){
        user = $("#user_name").val();
        drawGraph();

    });
    

});

