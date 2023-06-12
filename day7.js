const { dir } = require('console');
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

// Part 2 Runner Code.
const totalSpace = 70000000
const neededUnusedSpace = 30000000;
currentDirectory = ['/'];
const neededSpace = neededUnusedSpace - (totalSpace - sizeOfDirectory(cache['/']));
currentDirectory = [];
let min = Infinity;
for(let key in cache) {
    currentDirectory.push(key);
    let dirSize = sizeOfDirectory(cache[key]);
    if (dirSize >= neededSpace && dirSize < min) {
        min = dirSize;
    }
}
console.log(min);