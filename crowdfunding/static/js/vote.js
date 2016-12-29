$("#VoteBtn").click(function () {
    alert('UpVoting');
    var post_id = $(this).attr('data-post-id');

    $.ajax({
        url: '/crowdfunding/vote/',
        data: {
            'post_id': post_id,
            'vote_type': 'UP'
        },
        dataType: 'json',
        success: function (data) {
            if (data.success) {
                alert(data.upvote);
                $('#VoteBtn').attr("disabled", true);
                $('#VoteBtnDown').attr("disabled", true);
                $("#VoteBtn").html(data.upvote);
            }
            else{
                $('#VoteBtn').removeAttr("disabled");
                $('#VoteBtnDown').removeAttr("disabled");
            }
        }
    });

});


$("#VoteBtnDown").click(function () {
    alert('DownVoting');
    var post_id = $(this).attr('data-post-id');

    $.ajax({
        url: '/crowdfunding/vote/',
        data: {
            'post_id': post_id,
            'vote_type': 'DN'
        },
        dataType: 'json',
        success: function (data) {
            if (data.success) {
                $('#VoteBtn').attr("disabled", true);
                $('#VoteBtnDown').attr("disabled", true);
                $("#VoteBtnDown").html(data.downvote);
            }
            else{
                $('#VoteBtn').removeAttr("disabled");
                $('#VoteBtnDown').removeAttr("disabled");
            }
        }
    });

});