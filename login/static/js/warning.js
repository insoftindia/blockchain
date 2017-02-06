$("#register-username").change(function () {
    var username = $(this).val();
    $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                $('.form-control-feedback').show();
                $('#register_button').attr("disabled", true);
            }
            else{
                $('.form-control-feedback').hide();
                $('#register_button').removeAttr("disabled");
            }
        }
    });

});
