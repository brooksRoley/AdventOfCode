const fs = require('fs');
const input = fs.readFileSync('./day9input.txt', 'utf8').split('\n');

class Head {
    constructor() {
        this.x = 0;
        this.y = 0;
        this.Tail = new Tail();
        this.moves = {
            'U': () => this.y += 1,
            'D': () => this.y -= 1,
            'R': () => this.x += 1,
            'L': () => this.x -= 1,
        }
    }
    checkTail(x, y) {
        let xd = Math.abs(this.x - this.Tail.x);
        let yd = Math.abs(this.y - this.Tail.y);
        if(xd > 1 || yd > 1) {
            console.log(x, y);
            this.Tail.addMap();
            this.Tail.x = x;
            this.Tail.y = y;
        }
    }
    move(direction, n) {
        for(let i=0; i<parseInt(n); i++) {
            let tempx = this.x;
            let tempy = this.y;
            this.moves[direction]();
            this.checkTail(tempx, tempy);
        }
    }
}

class Tail {
    constructor() {
        this.x = 0;
        this.y = 0;
        this.map = new Set();
    }

    addMap() {
        this.map.add(`${this.x},${this.y}`);
    }
}

const snake = new Head();
for(let i=0; i<input.length; i++){
    let [dir, n] = input[i].split(' ');
    console.log(dir, n);
    snake.move(dir, n);
}
snake.Tail.addMap();
console.log(snake.Tail.map.size);
// Part 2