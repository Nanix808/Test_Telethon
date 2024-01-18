document.getElementById("send_message").addEventListener("submit", function(event){
    event.preventDefault()
  
    var xhr = new XMLHttpRequest();
   
    xhr.open("POST", '/api/messages/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        message_text: document.getElementById("message_text").value,
        from_phone: document.getElementById("send_phone").value,
        username: document.getElementById("username").value
      }));
  
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      console.log(data);
     
  
    };
  });