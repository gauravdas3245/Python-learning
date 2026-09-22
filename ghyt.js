function calculateTotal(numbers) {
    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total = total + numbers[i];
    }

    return total;
}

function getStatus(total, target = 100) {
    if (total >= target) {
        return "Target Reached";
    } else {
        return "Target Not Reached";
    }
}

let total = calculateTotal([20, 35, 50]);

console.log(total);
console.log(getStatus(total));







function countEvenNumbers(numbers) {
    let count = 0;

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 != 0) {
            continue;
        }

        count++;
    }

    return count;
}

console.log(countEvenNumbers([3, 8, 11, 14, 20]));












function firstFail(marks, passMark = 40) {
    let index = -1;

    for (let i = 0; i < marks.length; i++) {
        if (marks[i] < passMark) {
            index = i;
            break;
        }
    }

    return index;
}

console.log(firstFail([65, 72, 33, 80]));