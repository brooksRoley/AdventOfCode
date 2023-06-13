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

// During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420. (The 20th cycle occurs in the middle of the second addx -1, so the value of register X is the starting value, 1, plus all of the other addx values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
// During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.
// During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.
// During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.
// During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.
// During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.
