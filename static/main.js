const addMessage = (data) => {

    let messageBox = null;

    if(data['username'] && data['message']){

        let current_time = new Date();

        let formatted_time = `${current_time.getHours()}:${current_time.getMinutes()}`

        if(username !== data["username"]){
            messageBox = 
            '<div class = "message-container-left">' + 
                '<p class = "user-info">' + `${data['username']}, ${formatted_time}` + '</p>' + 
                '<div class = "message-left">'+
                     data['message'] +
                 '</div>' + 
            '</div>'

        }else{
            messageBox = 
            '<div class = "message-container-right">' + 
                '<p class = "user-info">' + `You, ${formatted_time}` + '</p>' + 
                '<div class = "message-right">'+
                     data['message'] +
                 '</div>' + 
            '</div>'
        }
    }

    return messageBox;

}

// http://127.0.0.1:5000

//"http://" + document.domain + ":" + location.port)

var socket = io();

socket.on('connect', function (){


    if (username !== ""){
        socket.emit('join', {
            username : username.charAt(0).toUpperCase() + username.slice(1),
            room : room
        })
    }

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {

        e.preventDefault();

        let messageInput = document.getElementById("message-input")

        if(messageInput.value.length){

            let message = messageInput.value.trim();

            socket.emit('message', {
                username : username,
                room : room,
                message : message
            });
        
            messageInput.value = '';
            messageInput.focus();      

        }        
    })
})

socket.on('join_room_announcement', function(data){
    const joinedMessage = document.createElement('div');
    joinedMessage.innerHTML = `<p class="join-room-announcement">*<b>${data.username}</b> has joined chat room ${data.room}*</p>`;
    document.getElementById('chat-display').appendChild(joinedMessage);
});

socket.on('recieve_message', function(data){
    const message = document.createElement('div');
    message.innerHTML = addMessage(data);
    document.getElementById('chat-display').appendChild(message);
});