jQuery(document).ready(function($) {

    $("#VoteBtn").click(function () {
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
                    $("#VoteBtn").html(data.upvote);
                    $("#VoteBtnDown").html(data.downvote);
                }
            }
        });
    });

    $("#VoteBtnDown").click(function () {
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
                    $("#VoteBtn").html(data.upvote);
                    $("#VoteBtnDown").html(data.downvote);
                }
            }
        });
    });

    $("#btn-close-proposal").click(function () {
        var post_id = $(this).attr('data-post-id');
//        alert("FFFFFFFFFFFFFFFFFFFFFF");
        $.ajax({
            url: '/crowdfunding/close_proposal/',
            data: {
                'post_id': post_id,
            },
            dataType: 'json',
            success: function (data) {

            }
        });
    });

});