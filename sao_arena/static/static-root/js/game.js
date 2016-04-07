$(document).ready(function() {
    $('iron-icon').click(function(){
        $('.selected').removeClass('selected'); // removes the previous selected class
        $(this).addClass('selected'); // adds the class to the clicked image  
    });        
});


function EndTurn(player_id) {
    getGameInfo(player_id);
    //updateCharacterStats(character_id);
    updateGameUI(player_id);
}

function getGameInfo(player_id){ 
        $.ajax({
            type: 'GET',
            url: '/api/game/players/' + player_id + '/',
            success: function (data){
                console.log(data);
                
                var character1 = data.active_character_1.id
               //getGameJSON(player_id);
            },
            statusCode: {
                404: function() {
                alert( "404 Error" );
            }},
            error: function () {
                alert('Error: failed to join game');
            }, 
        })
        
        
}

function updateGameUI(player_id){ 
        $.ajax({
            type: 'GET',
            url: '/api/game/players/' + player_id + '/',
            success: function (data){
                console.log(data);
            
            var health1 = data.active_character_1.health;
            //console.log(health);
            $('#character1').attr("health", String(health1));
            
            var health2 = data.active_character_2.health;
            $('#character2').attr("health", String(health2));
            
            var health3 = data.active_character_3.health;
            $('#character3').attr("health", String(health3));
               
            },
            statusCode: {
                404: function() {
                alert( "404 Error" );
            }},
            error: function () {
                alert('Error: failed to join game');
            }, 
        })
        
        
}


function updateCharacterStats(character_id){
    $.ajax({
            type: 'GET',
            url: '/api/game/character-stats/' + id + '/',
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