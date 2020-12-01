
let currInd = 0;
let code = [
    1,0,0,3,1,1,2,3,1,3,
    4,3,1,5,0,3,2,6,1,19,
    1,19,10,23,2,13,23,27,1,5,
    27,31,2,6,31,35,1,6,35,39,2,
    39,9,43,1,5,43,47,1,13,47,51,1,
    10,51,55,2,55,10,59,2,10,59,63,1,
    9,63,67,2,67,13,71,1,71,6,75,
    2,6,75,79,1,5,79,83,2,83,9,87,
    1,6,87,91,2,91,6,95,1,95,6,99,
    2,99,13,103,1,6,103,107,1,2,107,
    111,1,111,9,0,99,2,14,0,0
];
let codeCopy = [];
for(let i = 0; i < code.length; i++) {
    codeCopy.push(code[i]);
}
let status = false;
let noun = 0;
let verb = 0;


function addVals(code, first, second, third) {
    code[third] = code[first] + code[second];
    return code;
}

function multVals(code, first, second, third) {
    code[third] = code[first] * code[second];
    return code;
}

loops:
for(let i = 0; i < 100; i++) {
    for(let j = 0; j < 100; j++) {
        code[1] = i;
        code[2] = j;

        while(code[currInd] != 99) {
            if(code[currInd] == 1) {
                code = addVals(code, code[currInd + 1], code[currInd + 2], code[currInd + 3]);
            } else if(code[currInd] == 2) {
                code = multVals(code, code[currInd + 1], code[currInd + 2], code[currInd + 3]);
            } else {
                console.log("Unknown opcode read: ", code[currInd]);
                break;
            }
            currInd += 4;
        }

        if(code[0] == 19690720) {
            status = true;
            noun = i;
            verb = j;
            break loops;
        }
        
        for(let n = 0; n < code.length; n++) {
            code[n] = codeCopy[n];
        }
        currInd = 0;

    }
}
if(status) {
    console.log("100 * noun + verb: ", 100 * noun + verb);
} else {
    console.log("Didn't Work");
}
console.log("Last opcode: ", code[currInd]);
console.log('Last index: ', currInd);

console.log('code[0]: ', code[0]);