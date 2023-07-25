const fs = require('fs');
const { parse } = require('path');
class Monkey {
    constructor() {
        this.id = null;
        this.items = [];
        this.operation = null;
        this.operationNumber = null;
        this.throw = null;
        this.count = 0;
    }
}
function extractNumbers(line) {
    return line.match(/\d+/g) ? line.match(/\d+/g).map(Number) : [];
}
function extractSymbol(line) {
    return line.match(/[\+\-\*\/]/g).map(String)[0];
}
function mapToOperationFunction(operator) {
    switch (operator) {
      case '+':
        return (a, b) => a + b;
      case '-':
        return (a, b) => a - b;
      case '*':
        return (a, b) => a * b;
      case '/':
        return (a, b) => a / b;
      default:
        throw new Error(`Unsupported operator: ${operator}`);
    }
}
function mapThrow(test, door1, door2) {
    return (item) => {
        return item % test === 0 ? door1.toString() : door2.toString();
    };
}
let superModulo = 1;
function parseMonkey(monkey) {
    const m = new Monkey(monkey);
    const name = extractNumbers(monkey[0]);
    m.id = name[0];

    const items = extractNumbers(monkey[1]);
    m.items = items;

    const operation = extractSymbol(monkey[2])
    const operationNumber = extractNumbers(monkey[2]);
    m.operation = mapToOperationFunction(operation);
    m.operationNumber = operationNumber;

    const test = extractNumbers(monkey[3])[0];
    superModulo *= test;

    const door1 = extractNumbers(monkey[4])[0];
    const door2 = extractNumbers(monkey[5])[0];
    m.throw = mapThrow(test, door1, door2);

    return m;
}

let monkeys = {};

let inputD = fs.readFileSync('day11input.txt', 'utf8');
inputD.toString().split("\n\n").forEach(stringSet => {
    const monkey = parseMonkey(stringSet.split("\n"));
    monkeys[monkey.id] = monkey;
});
for(let i = 0; i < 10000; i++) {
    Object.keys(monkeys).forEach(id => {
        let monkey = monkeys[id];
        for(let j = 0; j < monkey.items.length; j++) {
            let worry = monkey.items[j];
            let opvalue = monkey.operationNumber.length > 0 ? monkey.operationNumber[0] : worry;
            worry = monkey.operation(worry, opvalue);

            // If it doesn't mess with any of the modulus tests defined by the monkeys*
            // We can reduce the worry level by that multiple.
            worry = worry % superModulo;

            let nextMonkeyId = monkey.throw(worry);
            let nextMonkey = monkeys[nextMonkeyId];
            nextMonkey.items.push(worry);
        }
        monkeys[id].count += monkey.items.length;
        monkeys[id].items = [];
    });
}
let ranked = Object.keys(monkeys).map(m => monkeys[m].count).sort((a, b) => b - a);
console.log(ranked);
console.log(ranked[0] * ranked[1]);