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
                    location.reload(true);
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
                    location.reload(true);
                }
            }
        });
    });

    $("#btn-close-proposal").click(function () {
        var post_id = $(this).attr('data-post-id');
        $.ajax({
            url: '/crowdfunding/close_proposal/',
            data: {
                'post_id': post_id,
                'user_id': 1,
            },
            dataType: 'json',
            success: function (data) {
                location.reload(true);
                var Web3 = require('web3');
                var web3 = new Web3();
//                web3.setProvider(new web3.providers.HttpProvider('http://ingethfyi.southindia.cloudapp.azure.com:8545'));
                web3.setProvider(new web3.providers.HttpProvider('http://ingethzsz.eastasia.cloudapp.azure.com:8545'));
                var tx = {from: web3.eth.coinbase, to: '0x97075926C58DCb09B67DeB9D208F7ddaf0947383', value: web3.toWei(data.amount, "ether")}
                web3.eth.sendTransaction(tx, "Insoftindia@ether");

            }
        });
    });

    $("#btn-rejection-proposal").click(function () {
        var post_id = $(this).attr('data-post-id');
        $.ajax({
            url: '/crowdfunding/rejection_proposal/',
            data: {
                'post_id': post_id,
                'user_id': '1'
            },
            dataType: 'json',
            success: function (data) {
                location.reload(true);
            }
        });
    });

    function comment_submit(post_id){
        var comment_text = $('#comment-text').val();
        if( comment_text ) {
            $.ajax({
                url: '/crowdfunding/post_comment/',
                data: {
                    'post_id': post_id,
                    'comment_text':comment_text
                },
                dataType: 'json',
                success: function (data) {
                    location.reload(true);
                }
            });
        }
    }

    $("#btn-submit-comment").click(function () {
        var post_id = $(this).attr('data-post-id');
        comment_submit(post_id);
    });

    $('#comment-text').keydown(function(event) {
        if (event.keyCode == 13) {
            var post_id = $(this).attr('data-post-id');
            comment_submit(post_id);
         }
    });

//    Reply

    function comment_reply_submit(post_id){
        var comment_text = $('#comment-text').val();
        if( comment_text ) {
            $.ajax({
                url: '/crowdfunding/post_comment/',
                data: {
                    'post_id': post_id,
                    'comment_text':comment_text
                },
                dataType: 'json',
                success: function (data) {
                    location.reload(true);
                }
            });
        }
    }

    $("#btn-submit-comment-reply").click(function () {
        var post_id = $(this).attr('data-post-id');
        var comment_id = $(this).attr('data-comment-id');
        comment_submit(post_id);
    });

    $('#comment-text-reply').keydown(function(event) {
        if (event.keyCode == 13) {
            var post_id = $(this).attr('data-post-id');
            var comment_id = $(this).attr('data-comment-id');
            comment_submit(post_id);
         }
    });



});
