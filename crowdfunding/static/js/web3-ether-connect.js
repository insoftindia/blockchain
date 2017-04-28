jQuery(document).ready(function($) {

    var user_id = $('#user-data').attr('data-user-id');
    $.ajax({
        url: '/crowdfunding/get_user_private_key/',
        data: {
            'user_id': user_id,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data);
            var Web3 = require('web3');
            var web3 = new Web3();
//            web3.setProvider(new web3.providers.HttpProvider('http://ingethfyi.southindia.cloudapp.azure.com:8545'));
            web3.setProvider(new web3.providers.HttpProvider('http://ingethzsz.eastasia.cloudapp.azure.com:8545'));
            var originalBalance = web3.fromWei(web3.eth.getBalance(data.key).toNumber(), "ether");
            $("#ether-balance").html(originalBalance);
        }
    });


    $("#ether-tranfer").click(function () {
        event.preventDefault();
        var user_id = $('#user-data').attr('data-user-id');
        var ether = $('#ether-amount-input').val();
        var account = $('#account-input').val();

        $.ajax({
            url: '/crowdfunding/get_user_private_key/',
            data: {
                'user_id': user_id,
            },
            dataType: 'json',
            success: function (data) {
                var Web3 = require('web3');
                var web3 = new Web3();
//                web3.setProvider(new web3.providers.HttpProvider('http://ingethfyi.southindia.cloudapp.azure.com:8545'));
                web3.setProvider(new web3.providers.HttpProvider('http://ingethzsz.eastasia.cloudapp.azure.com:8545'));
                var tx = {from: web3.eth.coinbase, to: account, value: web3.toWei(ether, "ether")}
                web3.eth.sendTransaction(tx, "Insoftindia@ether");
//                web3.personal.unlockAccount(web3.eth.coinbase, 'Insoftindia@ether');
//                web3.eth.sendTransaction({from: web3.eth.coinbase, to: account, value: web3.toWei(ether, "ether")})
            }
        });
        $('#transfer-ether').modal('toggle')
    });
});