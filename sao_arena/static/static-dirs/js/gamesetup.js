
$('#join-game-form').submit(function(e){
    e.preventDefault();
    alert('new submit');
    joinGame($("#player_id").html());
});

$(document).ready(function() {
 // executes when complete page is fully loaded, including all frames, objects and images
 getGameJSON($("#player_id").html())
});

function onJoinButtonClick() {
    $('#join_button').hide();
}

function goToGame() {
    $('#game-home').hide();
    $('#game-start').show();
}

function joinGame(player_id){
        onJoinButtonClick();
        
        $.ajax({
            type: 'POST',
            url: '/api/game/join/' + player_id + '/',
            success: function (){
                alert('Success joined game');
                getGameJSON(player_id);
            },
            statusCode: {
                404: function() {
                //alert( "404 Error" );
                getGameJSON(player_id);
            }},
            error: function () {
                //alert('Error: failed to join game');
            }, 
        })
        
        
}


function getGameObjectJSON(id){
    $.ajax({
            type: 'GET',
            url: '/api/game/games/' + id + '/',
            success: function (data){
                //alert(JSON.stringify(data));
                $('#JSON').html(JSON.stringify(data));
                goToGame();
                return JSON.stringify(data);
            },
            statusCode: {
                404: function() {
                alert( "404: Game does not exist" );
            }},
            error: function () {
                //alert('Error: failed to join game');
            }, 
        })
}


function getGameJSON(player_id) {
    $.ajax({
            type: 'GET',
            url: '/api/game/games/by-player/' + player_id + '/',
            success: function (data){
                //alert('Success got info');
                $('#join_button').hide();
                $('#JSON').innerHTML=("<p>" + getGameObjectJSON(data.id) + "</p>");
                
                window.location = "http://localhost:8000/game/start/" + player_id + "/";
                
            },
            statusCode: {
                404: function() {
                //alert( "404 Error" );
                getGameJSON(player_id);
            }},
            error: function () {
                //alert('Error: did not get info');
            }, 
        })
}