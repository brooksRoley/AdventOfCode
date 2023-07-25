// Maybe you can learn something by looking at the value of the X register throughout execution.
// For now, consider the signal strength (the cycle number multiplied by the value of the X register)
// during the 20th cycle and every 40 cycles after that
// (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

const fs = require('fs');
const input = fs.readFileSync('./day10input.txt', 'utf8').split('\n');


let sum = 0;
let cycle = 0;
let x = 1;
let add = [0, 0]
let triggers = [20, 60, 100, 140, 180, 220];

function checkCycle() {
    if(triggers.includes(cycle)) {
        // console.log(cycle, x, cycle * x);
        sum += cycle * x;
    }
}

for(let i=0; i<input.length; i++){
    let line = input[i].split(' ');
    cycle += 1;
    checkCycle();
    if(line[0]== 'addx') {
        cycle += 1;
        checkCycle();
        x += parseInt(line[1]);
    }
}
console.log(sum);
