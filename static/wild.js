document.getElementById("get_goods").addEventListener("submit", function(event){
    event.preventDefault()
  
    var xhr = new XMLHttpRequest();
    var params = 'goods='+ document.getElementById("name_goods").value;
    xhr.open("GET", '/api/wild/' + '?' + params, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
  
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      console.log(data);
      document.getElementById("text_goods").value = JSON.stringify(data);
    
  
    };
  });