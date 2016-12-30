jQuery(document).ready(function($) {

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

});