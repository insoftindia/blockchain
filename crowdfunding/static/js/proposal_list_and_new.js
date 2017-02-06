jQuery(document).ready(function($) {

    $(this).on('change', '#sel1', function(e){
        if (this.value=='MR'){
            $(this).parents('form').find('#funding_amout').css('visibility', 'visible');;

        }else {
            $(this).parents('form').find('#funding_amout').css('visibility', 'hidden');;
        }
    });

    function _get_group_total_amt() {
        var group_type = $('#group-type').val();
        var proposal_amount = $('#amount-input').val();
        var total_amount;
        $.ajax({
            url: '/crowdfunding/get_group_total_amount/',
            data: {
                'group_type': group_type,
            },
            dataType: 'json',
            success: function (data) {
                if (data.total_amt) {
                    $("#group-total-amount-input").val(parseFloat(data.total_amt).toFixed(2));
                    total_amount = data.total_amt;
                    _check_proposal_amount(proposal_amount, total_amount);
                }
                else {
                    $("#group-total-amount-input").val(parseFloat(0.00).toFixed(2));
                    total_amount = 0.00;
                    _check_proposal_amount(proposal_amount, total_amount);
                }
            }
        });

    }
    _get_group_total_amt();
     $("#group-type").change(function () {
        _get_group_total_amt();
     });

    function _check_proposal_amount(proposal_amount, total_amt) {
        if (parseFloat(proposal_amount) > parseFloat(total_amt)) {
            $('.amount-warning-msg').show();
            $('#proposal-post').attr("disabled", true);
        }
        else {
            $('.amount-warning-msg').hide();
            $('#proposal-post').removeAttr("disabled");
        }
    }

    $("#amount-input").change(function () {
        var proposal_amount = $('#amount-input').val();
        var total_amt = $('#group-total-amount-input').val();
        _check_proposal_amount(proposal_amount, total_amt);
    });

    $(function() {
        // Create the close button
        var closebtn = $('<button/>', {
            type:"button",
            text: 'x',
            id: 'close-preview',
            style: 'font-size: initial;',
        });
        closebtn.attr("class","close pull-right");
        // Set the popover default content
        $('.image-preview').popover({
            trigger:'manual',
            html:true,
            title: "<strong>Preview</strong>"+$(closebtn)[0].outerHTML,
            content: "There's no image",
            placement:'bottom'
        });
        // Clear event
        $('.image-preview-clear').click(function(){
            $('.image-preview').attr("data-content","").popover('hide');
            $('.image-preview-filename').val("");
            $('.image-preview-clear').hide();
            $('.image-preview-input input:file').val("");
            $(".image-preview-input-title").text("Browse");
        });
        // Create the preview image
        $(".image-preview-input input:file").change(function (){
            var img = $('<img/>', {
                id: 'dynamic',
                width:250,
                height:200
            });
            var file = this.files[0];
            var reader = new FileReader();
            // Set preview image into the popover data-content
            reader.onload = function (e) {
                $(".image-preview-input-title").text("Change");
                $(".image-preview-clear").show();
                $(".image-preview-filename").val(file.name);
                img.attr('src', e.target.result);
                $(".image-preview").attr("data-content",$(img)[0].outerHTML).popover("show");
            }
            reader.readAsDataURL(file);
        });
    });
    var deadline = new Date(Date.parse('January 20 2017 17:00:00'));
initializeClock('clockdiv', deadline);
function initializeClock(id, endtime) {
        var clock = document.getElementById(id);
        var daysSpan = clock.querySelector('.days');
        var hoursSpan = clock.querySelector('.hours');
        var minutesSpan = clock.querySelector('.minutes');
        var secondsSpan = clock.querySelector('.seconds');

        function updateClock() {
            var server_time = new Date();
            var t = getTimeRemaining(endtime, server_time);
            daysSpan.innerHTML = ('0' + t.days).slice(-2);
            hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
            minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
            secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);
            if (t.total <= 0) {
                clearInterval(timeinterval);
            }
        }
        updateClock();
        var timeinterval = setInterval(updateClock, 1000);
    }
    function getTimeRemaining(endtime, current_time) {
        var t = Date.parse(endtime) - current_time;
        var seconds = Math.floor((t / 1000) % 60);
        var minutes = Math.floor((t / 1000 / 60) % 60);
        var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
        var days = Math.floor(t / (1000 * 60 * 60 * 24));
        return {
            'total': t,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        };
    }

});