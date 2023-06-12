const fs = require('fs');
const input = fs.readFileSync('./day7input.txt', 'utf8').split('\n');
let currentDirectory = [];
let cache = {};

// Recursively calculate size of directory.
// For each element of our directory,
// we sum file sizes when we encounter a number.
// When we see a directory, we push it to our currentDirectory and recurse.
function sizeOfDirectory(dir, size=0) {
    for(let i=0; i<dir.length; i++) {
        const entry = dir[i];
        if(/^[0-9]*$/.test(entry)) {
            size += parseInt(entry);
        } else if (/^[A-Za-z]*$/.test(entry)) {
            currentDirectory.push(entry);
            size += sizeOfDirectory(cache[currentDirectory.join('/')]);
        }
    }
    currentDirectory.pop();
    return parseInt(size);
}

function command(line) {
    switch(line[1]) {
        case 'cd':
            if(line[2] == '..') {
                currentDirectory.pop();
            } else {
                currentDirectory.push(line[2]);
            }
            break;
        case 'ls':
            cache[currentDirectory.join('/')] = [];
            break;
        default:
            console.log('invalid command');
    }
}

// Loop over input and execute commands
// Adding files and directories to cache
for(let i = 0; i < input.length; i++) {
    let line = input[i].split(' ');
    if(line[0] == '$') {
        command(line);
    } else if (line[0] == 'dir') {
        cache[currentDirectory.join('/')].push(line[1]);
    } else {
        let size = line[0];
        let file = line[1];
        cache[currentDirectory.join('/')].push(size);
    }
}

// When we have our filesystem built from the input commands,
// we can loop over the cache and sum the size of each directory thats small enough.
let sum = 0;
currentDirectory = [];
for(let key in cache) {
    currentDirectory.push(key);
    let dirSize = sizeOfDirectory(cache[key]);
    if (dirSize <= 100000) {
        sum += dirSize;
    }
}
// console.log(cache);
console.log(sum);