document.getElementById("check_login").addEventListener("submit", function(event){
  event.preventDefault()

  var xhr = new XMLHttpRequest();
  var params = 'phone='+ document.getElementById("phone").value;
  xhr.open("GET", '/api/check/login' + '?' + params, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();

  xhr.onload = function () {
    var data = JSON.parse(xhr.responseText);
    console.log(data);
    document.getElementById("span_check_login").innerHTML = data.status;

  };
});
