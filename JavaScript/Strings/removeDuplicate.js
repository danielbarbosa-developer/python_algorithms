const prompt = require('prompt-sync')();

var initialString = prompt('Enter the string: ');

var verify = '';
var repetitions = 0;
var newArray = [];
var removedChars = [];


for(i=0; i<initialString.length; i++){
    //verification initializes only after the first iteration
    if(verify===initialString[i]){
        removedChars[repetitions] = initialString[i]; // it creates an array with only the repeated letters
        repetitions++;
        console.log('duplicate content');
        continue;
    }
    console.log(initialString[i]);
    verify = initialString[i];
    newArray[i-repetitions] = initialString[i];
}
console.log(removedChars);// array with only the repeated letters
console.log(newArray);// filtered array without repetitions