// Read the content of out11.txt using AJAX
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("sk1").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out21.txt", true);
xhttp.send();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("sk2").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out22.txt", true);
xhttp.send();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("sk3").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out23.txt", true);
xhttp.send();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("sk4").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out24.txt", true);
xhttp.send();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("sk5").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out25.txt", true);
xhttp.send();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("pt1").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out3.txt", true);
xhttp.send();
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var newText = this.responseText;
    // Update the HTML of the element with class 'in1'
    document.getElementById("ch2").innerHTML = newText;
  }
};
xhttp.open("GET", "static/out11.txt", true);
xhttp.send();
