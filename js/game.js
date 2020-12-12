console.log("hello");
// https://v42v8t.deta.dev/
// this is api url
dataSlug = [
4521,
3895,
1235,
7854,
1256,
9561,
3644,
4932,
1099,
1007,
]

// console.log(dataSlug[2]);

const hintText = document.querySelector(".game__clueText")
const first = document.querySelector("#ist")
const sec = document.querySelector("#sec")
const third = document.querySelector("#third")
const fourth = document.querySelector("#fourth")
const check = document.querySelector(" button")
const frm = document.querySelector("form")

const API = "https://v42v8t.deta.dev/"


let i = 0;

// let slugCode = dataSlug[i];

var codeSlug

var code = '';
//  console.log(code);

function gameClue (i){
    fetch(`${API}${dataSlug[i]}`).then(
        res => res.json()
    ).then(
        dataDisplay
    ) 
}

function dataDisplay (e){
    clue = e["clue"];
    console.log(clue);
    hintText.innerHTML = clue;
    codeSlug = e["code"]
    checkClue(codeSlug);
}

function checkClue(e){
    console.log(e);

}

function showDD (e){
    console.log(e.data);
     let ce = e.data;
    // code.push(e.data)
    code += ce;
    // console.log(ce);
    console.log(code);
}

checkBTN = (e)=>{
    e.preventDefault()
    if(codeSlug != "0000")
    {if(code === codeSlug)
    {console.log(codeSlug);
    gameClue(++i)}else{
        location.href="./loose.html"
    }
    frm.reset()
    code = ""}else{
        location.href="./win.html"
    }
}


window.onload = gameClue(i);




first.addEventListener('input', showDD)
sec.addEventListener('input', showDD)
third.addEventListener('input', showDD)
fourth.addEventListener('input', showDD)



check.addEventListener('click', checkBTN)