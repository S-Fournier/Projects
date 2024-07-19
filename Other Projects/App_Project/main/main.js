var options_data = localStorage.getItem('options_data');
var options_data = JSON.parse(options_data);
var default_activity_list = options_data.default_activity_list;
//var frequency = Number(options_data.frequency)*60000;
var frequency = 3000;
var stop = options_data.stop;
var save_info = {};
var stats = {};
var activities = [];
var check = [];
var score = [];
var score_max = 0;

for(let i = 0; i < default_activity_list.length; i++){
    activities.push(default_activity_list[i]);
    check.push(false);
    score.push(0);
}

interval = setInterval(timer,60000);


function timer() {
    var clock = new Date();
    clock = clock.getHours() + ":" + clock.getMinutes();
    if(clock >= stop){
        clearTimeout(timeout);
        clearInterval(interval);
        reset();
        end();
    }
}

function start() {
    document.getElementById("check").style.display = "none";
    document.getElementById("initial").style.display = "none";
    timeout = setTimeout(display_checkpoint, frequency);
    
}

function reset() {
    document.getElementById("checklist_ul").innerHTML = "";
    check = [];
}

function display_checkpoint() {
    document.getElementById("check").style.display = "block";
    let ul = document.getElementById("checklist_ul");

    for (let i = 0; i < activities.length; i++) {
        let li = document.createElement("li");
        let li_text = document.createTextNode(activities[i]);
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.id = activities[i];

        ul.appendChild(li);
        li.appendChild(li_text);
        li.appendChild(checkbox);
    }
}

function submit() {

    for (let i = 0; i < activities.length; i++) {
        let x = document.getElementById(activities[i]);
        check[i] = x.checked;
        if(x == true){
            score[i] = score[i] + 1;
        }
    }

    score_max = score_max + 1;
    
    let date = new Date();
    let time = date.getHours() + ":" + date.getMinutes();
    
    save_info[time] = {};
    
    for (let i = 0; i < activities.length; i++){
        save_info[time][activities[i]] = check[i];
    }

    console.log(save_info);

    reset();
    start();
}

function add_to_list() {

    let activity = document.getElementById("to_do_activity").value;
    let li = document.createElement("li");
    let li_text = document.createTextNode(activity);
    let span = document.createElement("SPAN");
    let span_text = document.createTextNode("\u00D7");

    span.appendChild(span_text);
    li.appendChild(li_text);
    li.appendChild(span);

    activities.push(activity);
    check.push(false);
    score.push(0);

    document.getElementById("display_list").appendChild(li);
    document.getElementById("to_do_activity").value = "";

    span.addEventListener("click", function() {
        let li = this.parentElement
        let i = activities.indexOf(input_value);
        li.style.display = "none";
        activities.splice(i,1);
        check.splice(i, 1);
        score.splice(i, 1);
    });
}



function end() {
    for(let i = 0; i < activities.length; i++) {
        let li = document.createElement("li");
        let li_text = document.createTextNode(activities[i]);
        let span = document.createElement("span");
        let x = score[i] / score_max * 100
        let span_text = document.createTextNode(x + "%")

        li.appendChild(li_text);
        li.appendChild(span);
        li.appendChild(span_text);

        document.getElementById("check").appendChild(li);       
    }
    let day = new Date();
    day = day.getFullYear() + "-" + day.getMonth() + "-" + day.getDay();

    stats[day] = save_info;

    localStorage.setItem('stats',JSON.stringify(stats));
}