var default_activity_list = [];
var frequency;
var stop;
var close = document.getElementsByClassName("close");

function save_interval_time() {
    var frequency = document.getElementById("interval_time").value;
    return frequency
}

function save_end_time() {
    var stop = document.getElementById("end_time").value;
    return stop
}

function add_to_list() {
    
    var default_activity = document.getElementById("default_activity").value;
    default_activity_list.push(default_activity);

    var li = document.createElement("li");
    var inputValue = document.getElementById("default_activity").value;
    var activity = document.createTextNode(inputValue);
    li.appendChild(activity);
    document.getElementById("display_list").appendChild(li);
    document.getElementById("default_activity").value = "";

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);
  
    for (let i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
            default_activity_list.splice(i, 1);
        }
    }
}