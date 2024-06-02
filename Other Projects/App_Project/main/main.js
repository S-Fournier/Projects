var to_do_activities = [];
var activities = [];
var check = [];
var break_times = [];
var main_obj = {};
var next = false;

function add_to_do_list() {
    var to_do_activiy = document.getElementById("to_do_activity").value;
    to_do_activities.push(to_do_activiy);
    document.getElementById("to_do_activity")="";
    input_display("display_to_do_list", "div", to_do_activities);
}

function start() {
    document.getElementById("frame").innerHTML="";
    for (let i=0; i<default_activity_list.length; i++) {
        activities.push(default_activity_list[i]);
    }
    for (let i=0; i<to_do_activities; i++) {
        activities.push(to_do_activities[i]);
    }
    for (let i=0; i<activities; i++) {
        check.push(false)
    }
    setTimeout(display_checkpoint,frequency)
}

function checkpoint() {
    let checkpoint_time = Date.now;
    break_times.push(checkpoint_time);
    main_obj[checkpoint_time] = {};
    for(let i=0; i<activities.length; i++){
        
    }

    display_input_data()
    
    if(checkpoint_time>=stop){
        end_day();
    }
    else {        
    }
}

function display_checkpoint() {
    var target_ID = document.getElementById("check");
    target_ID.innerHTML = "";

    for (let i = 0; i < activities.length; i++) {
        var new_checkbox = document.createElement("input");
        new_checkbox.type = "checkbox";
        new_checkbox.id = activities[i]
        target_ID.appendChild(new_checkbox);
    }

    var submit_button = document.createElement("button");
    submit_button.innerHTML = "Submit";
    submit_button.setAttribute("onclick","submit()");
    target_ID.appendChild(submit_button);
}

function submit() {
    for (let i = 0; i < check.length; i++) {
        var x = document.getElementById(test[i]);
        check[i] = x.checked;
    }
}