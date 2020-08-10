export function shuffle(array) {
    let counter = array.length;

    // While there are elements in the array
    while (counter > 0) {
        // Pick a random index
        let index = Math.floor(Math.random() * counter);

        // Decrease counter by 1
        counter--;

        // And swap the last element with it
        let temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}

export function sample(array,count){;
    let sampled = [];
    for (let i= 0; i < count;i++){
        sampled.push(array[Math.floor(Math.random()*array.length)])
    }
    return sampled
}

