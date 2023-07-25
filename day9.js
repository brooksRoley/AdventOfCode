const fs = require('fs');
const input = fs.readFileSync('./day9input.txt', 'utf8').split('\n');

const ROPE_LENGTH = 10;

class Knot {
    constructor(name='') {
        this.name = name;
        this.x = 0;
        this.y = 0;
        this.map = new Set([`0,0`]);
        this.tail = null;
    }
    moveHead() {
        return {
            'U': () => this.y += 1,
            'D': () => this.y -= 1,
            'R': () => this.x += 1,
            'L': () => this.x -= 1,
        }
    }
    motion() {
        this.addMap();
        if(!this.tail) { return; };

        let xd = Math.abs(this.x - this.tail.x);
        let yd = Math.abs(this.y - this.tail.y);
        // console.log(this.x, this.y)
        // console.log(xd, yd)

        // if(xd === 0 && yd === 0) { return; }
        // if(xd == 2 && yd == 0) {
        //     this.tail.x += xd/2;
        // }
        // if(yd == 2 && xd == 0) {
        //     this.tail.y += yd/2;
        // }
        // if(yd == 2 && xd == 2) {
        //     this.tail.x += xd/2; return;
        //     this.tail.y += yd/2; return;
        // };

        this.tail.motion(this.x, this.y);
    }
    move(d, n) {
        for(let i=0; i<parseInt(n); i++) {
            this.moveHead()[d]();
            this.motion();
        }
        
    }

    addMap() {
        this.map.add(`${this.x},${this.y}`);
    }
}

// Make the knot chain.
const snake = new Knot('0');
let cur = snake;
cur.tail = new Knot('1');
// for (let i = 1; i < ROPE_LENGTH; i++) {
//     cur = cur.tail;
// }

// Move the snake based on the input.
for(let i=0; i<input.length; i++){
    let [dir, n] = input[i].split(' ');
    snake.move(dir, n);
}

// Final list of visited points in the tail.
console.log(cur.map);
console.log(cur.map.size);