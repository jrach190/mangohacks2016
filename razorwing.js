$(document).ready(function(){
    user = "";
    
    $('#search').bind('keypress keydown', function(e){
       if(e.keyCode == 13) { e.preventDefault(); }
    });
    
    
    
    $("input[type=text]").keyup(function(e){
        if(e.keyCode == '13'){
            user = $("#user_name").val();
            $('p').text(user);
            $('img').hide();
            e.preventDefault();
            return false;
        }
        $(".jumbotron > .container > row > .col-md-4 > form").css("animation-play-state", "running");
        $(".jumbotron > .container > row > .col-md-4 > img").css({"animation-duration":"2s","animation-name":"query_user_img","animation-direction":"forward","animation-iteration-count":"1","animation-fill-mode":"forward"});

    });
    
    
    $("#submit").click(function(){
        user = $("#user_name").val();
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
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
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
            valueSuffix: 'Mood'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'Tokyo',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }]
    });

    });
    

});

