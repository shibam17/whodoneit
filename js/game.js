console.log("hello");
// https://v42v8t.deta.dev/
// this is api url
// /4521
// /3895
// /1235
// /7854
// /1256
// /9561
// /3644
// /4932
// /1099
// /1007

const hintText = document.querySelector(".game__clueText")

const API = "https://v42v8t.deta.dev/"

let slugCode = 4521;

function gameClue (){
    fetch(`${API}${slugCode}`).then(
        res => res.json()
    ).then(
        dataDisplay
    )
}

function dataDisplay (e){
    clue = e["clue"];
    console.log(clue);
    hintText.innerHTML = clue;
}



window.onload = gameClue();