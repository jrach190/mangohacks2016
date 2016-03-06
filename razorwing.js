mood = [];
text = [];
var data = new Array(10);
for (var i = 0; i < 10; i++) {
  data[i] = new Array(2);
}
pos = 0;
negs = 0;
neut = 0;

function getData(){
    data [0][0]= "Hello";
    data [1][0]= "Hello";
    data [2][0]= "Hello";
    data [3][0]= "Hello";
    data [4][0]= "Hello";
    data [5][0]= "Hello";
    data [6][0]= "Hello";
    data [7][0]= "Hello";
    data [8][0]= "Hello";
    data [9][0]= "Hello";
    
    data [0][1]= "negative";
    data [1][1]= "positive";
    data [2][1]= "positive";
    data [3][1]= "neutral";
    data [4][1]= "positive";
    data [5][1]= "positive";
    data [6][1]= "neutral";
    data [7][1]= "negative";
    data [8][1]= "negative";
    data [9][1]= "positive";
    return data;
}

function interpretData(data){
    for (i = 0; i < data.length; i++) {
       text[i] = data[i][0];
        mood[i] = data[i][1];
        if(mood[i] == "positive"){
            pos = pos + 1;
            mood[i] = 1;
        }else if(mood[i] == "negative"){
            negs = negs+1;
            mood[i] = -1;
        }else{
            neut = neut + 1;
            mood[i] = 0;
        }
        
     }
}

function drawGraph(){
    $(".jumbotron").css("height", "100%");
    twitter_data = getData();
    interpretData(twitter_data);
    $('#image-container').css('position', 'fixed')
    $('#image-container').remove();

    
    $('#graph').fadeIn()
        
    $('#graph').highcharts({
        title: {
            text: 'Mood Timeline',
            x: -20 //center
        },
        subtitle: {
            text: 'Source: Twitter.com',
            x: -20
        },
        xAxis: {
          tickInterval: 1,
          title: {
              text: 'Post'
          }
        },
        yAxis: {
            title: {
                text: 'Mood'
            },
            tickInterval: 1,
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
        },
        legend: {
            enabled: false
        },
        series: [{
            name: user,
            data: mood
        }]
    });
    
    pieChart();
    
}


function pieChart(){
    $('#pie').fadeIn()
    
    $('#pie').highcharts({
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
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            name: 'Mood',
            colorByPoint: true,
            data: [{
                name: 'Positive',
                y: (pos/(pos+negs+neut)),
                sliced: true,
                selected: true,
                color: '#00cc66'
            }, {
                name: 'Negative',
                y: (negs/(pos+negs+neut)),
                color: '#ff5050'
            }, {
                name: 'Neutral',
                y: (neut/(pos+negs+neut)),
                color: '#cfcfcf'
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

