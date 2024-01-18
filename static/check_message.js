document.getElementById("check_message").addEventListener("submit", function(event){
    event.preventDefault()
  
    var xhr = new XMLHttpRequest();
    var params = 'phone='+ document.getElementById("phone_check").value+'&'+'uname='+ document.getElementById("chat_id").value;
    xhr.open("GET", '/api/messages/' + '?' + params, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
  
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      console.log(JSON.stringify(data.data));
      document.getElementById("text_message").value = JSON.stringify(data.data);
  
    };
  });
  