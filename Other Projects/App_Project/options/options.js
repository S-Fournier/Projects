var default_activity_list = [];
var options_data = localStorage.getItem('options_data');

if(options_data !== null){
    var options_data = JSON.parse(options_data);
    var default_activity_list = options_data.default_activity_list;
    var frequency = Number(options_data.frequency)*60000;
    var stop = options_data.stop;
    for(let i = 0; i < default_activity_list.length; i++){
        let default_activity = default_activity_list[i];
        add_to_list(default_activity);
    }
}

function add_to_array() {
    let default_activity = document.getElementById("default_activity").value; //get value from target element   
    default_activity_list.push(default_activity); //append value into array for storage
    add_to_list(default_activity); //pass value to add_to_list function
}

function add_to_list(input_value) {
      
    let li = document.createElement("li"); //create a child li
    let li_text = document.createTextNode(input_value); //create text from input_value
    let span = document.createElement("SPAN"); //create close element
    let span_text = document.createTextNode("\u00D7"); //create x button

    span.appendChild(span_text);
    li.appendChild(li_text);
    li.appendChild(span);

    document.getElementById("display_list").appendChild(li); //append child li to parent ul
    document.getElementById("default_activity").value = ""; //delete target element's value
    
    span.addEventListener("click", function() {
        let li = this.parentElement
        let i = default_activity_list.indexOf(input_value);
        li.style.display = "none";
        default_activity_list.splice(i,1); 
    });
}

function save_settings() {
    var frequency = document.getElementById("interval_time").value;
    var stop = document.getElementById("end_time").value;
    var options_data = {'default_activity_list' : default_activity_list, 'frequency' : frequency, 'stop' : stop};
    localStorage.setItem('options_data', JSON.stringify(options_data));
}