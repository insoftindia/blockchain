$("#closeNav").hide();

$("#openNav").click(function () {
        $(this).hide();
        $.ajax({
            url: '/crowdfunding/make_history/',
            data: {
                'test': 'test',
            },
            dataType: 'json',
            success: function (data) {
                console.log(data);
                
                dddd = data['results'];
                
                var resultHtml = '';

                $.each(JSON.parse(dddd), function(key,value){     
                    resultHtml+='<div class="result">';
                    resultHtml+='<p>'
                    resultHtml+='<span>action time: '+ value.fields.action_time +'<span></br>';
                    resultHtml+='<span>change message: '+ value.fields.change_message +'<span></br>';
                    resultHtml+='<span>object: '+ value.fields.object_repr +'<span>';
                    resultHtml+='</p>'
                    resultHtml+='</div>';
                });

                $("#test2").html(resultHtml);
                
            }
        });
        document.getElementById("mySidenav").style.width = "300px";
        $("#closeNav").show();
});


$("#closeNav").click(function () {
    document.getElementById("mySidenav").style.width = "0";
    $("#openNav").show();
    $("#closeNav").hide();
});

