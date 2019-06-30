function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function grayscaleEffect(id){
    var currentTag = document.getElementById(id)
    for (let index = 100; index > -1; index--) {
        await sleep(25);
        currentTag.style["filter"] = "grayscale("+index+"%)";
    }
}

async function inverseEffect(id){
    var currentTag = document.getElementById(id)
    for (let index = 100; index > -1; index--) {
        await sleep(15);
        currentTag.style["filter"] = "invert("+index+"%)";
    }
}

async function hueRotateEffect(id){
    var currentTag = document.getElementById(id)
    for (let index = 360; index > -1; index--) {
        await sleep(5);
        currentTag.style["filter"] = "hue-rotate("+index+"deg)";
    }
}

async function blurEffect(id) {
    var currentTag = document.getElementById(id)
    for (let index = 10; index > -1; index--) {
        await sleep(15);
        currentTag.style["filter"] = "blur("+index+"px)";
    }
}