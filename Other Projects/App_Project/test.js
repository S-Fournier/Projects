var save_info = {};
var activities = [];
var check = [];
var break_times = [];
var frequency = 3000;
var date = new Date();


function start() {
    document.getElementById("frame").style.display = "none";
    setTimeout(display_checkpoint, frequency)
}

function submit() {
    for (let i = 0; i < activities.length; i++) {
        let x = document.getElementById(activities[i]);
        check[i] = x.checked;
    }
    for (let i = 0; i <activities.length; i++) {
        save_info[activities[i]] = check[i];
    }
}

function add_to_list() {

    let activity = document.getElementById("to_do_activity").value;
    let activity_text = document.createTextNode(activity);
    let li = document.createElement("li");
    let span = document.createElement("SPAN");
    let close_text = document.createTextNode("\u00D7");

    span.className = "close";
    span.appendChild(close_text);
    li.appendChild(activity_text);
    li.appendChild(span);

    activities.push(activity);
    check.push(false);

    document.getElementById("display_list").appendChild(li);
    document.getElementById("to_do_activity").value = "";

    var close = document.getElementsByClassName("close");

    for (let i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            let div = this.parentElement;
            div.style.display = "none";
            activities.splice(i, 1);
            check.splice(i, 1);
        }
    }
}

function display_checkpoint() {
    let target_ID = document.getElementById("check");

    for (let i = 0; i < activities.length; i++) {
        let li = document.createElement("li");
        let li_text = document.createTextNode(activities[i]);
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.id = activities[i];

        target_ID.appendChild(li);
        li.appendChild(li_text);
        li.appendChild(checkbox);
    }

    let submit_button = document.createElement("button");
    submit_button.innerHTML = "Submit";
    submit_button.setAttribute("onclick", "submit()");
    target_ID.appendChild(submit_button);
}