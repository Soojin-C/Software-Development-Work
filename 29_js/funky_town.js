//Team ArmorBuns - Wei Wen Zhou, Soojin Choi
//SoftDev1 pd8
//K29 -- Sequential Progression
//2018-12-19

var fibonacci = function(n) {
    // Returns the nth Fibonacci number

    // Why think when you can hard-code it haha!
    var list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765];

    if (n < list.length) {
        return list[n];
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

var gcd = function(a, b) {
    // Returns gcd of a, b
    var x;
    if (a < b) {
        x = a;
    } else {
        x = b;
    }
    while (x > 0) {
        if (a % x == 0 && b % x == 0) {
            return x;
        }
        x--;
    }
}

var randomStudent = function() {
    // Returns a random value from a list
    var list = ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad' ];
    return list[Math.floor(Math.random()*list.length)];
}

var randFib = function(){
    // Generates a random integer, n, between [0,25) and changes the text to the nth Fibonacci number
    randVal = Math.floor(Math.random() * 25);
    retVal = "fibonacci(" + randVal + ")" + " -> " + fibonacci(randVal);
    console.log(retVal);
    var textbox = document.getElementById('log');
    textbox.innerHTML = textbox.innerHTML + retVal+"<br>";
    return retVal;
};

var wipes = function() {
    // Resets the output section
    var textbox = document.getElementById('log');
    textbox.innerHTML = "Output: <br>"
    console.log("CLEAR!");
};

var chooseYourFib = function() {
    var textbox = document.getElementById('log');
    // Allows only numbers
    var num = parseInt(document.getElementById('number').value);
    if (!Number.isInteger(num)) {
        textbox.innerHTML = textbox.innerHTML + "Enter a number <br>";
        console.log("Enter a number");
        return;
    }
    // Limit the number of recursion calls.
    if (num > 50) {
        textbox.innerHTML = textbox.innerHTML + 'Stop yourself. This is not for your abuse <br> <a href="https://www.dcode.fr/fibonacci-numbers"> Find your nth Fibonacci number here </a> <br>';
        console.log("Stop yourself!");
        return;
    }

    // console.log(num + "?");
    retVal = "fibonacci(" + randVal + ")" + " -> " + fibonacci(num);
    console.log(retVal);
    textbox.innerHTML = textbox.innerHTML + retVal +"<br>";
    return retVal;
};

var randGCD = function(){
    // Generates random integers, a and b, between [0,100) and changes the text to the gcd of a and b
    a = Math.floor(Math.random() * 100);
    b = Math.floor(Math.random() * 100);

    retVal = "gcd of "+ a + " and " +b + " -> "+ gcd(a, b);
    console.log(retVal);

    var textbox = document.getElementById('log');
    textbox.innerHTML = textbox.innerHTML + retVal+"<br>";
    return retVal;
};

var chooseYourGCD = function(){
  var textbox = document.getElementById('log');
  //Allows only number
  var a = parseInt(document.getElementById('a').value);
  var b = parseInt(document.getElementById('b').value);
  if (!Number.isInteger(a) || !Number.isInteger(b)) {
      textbox.innerHTML = textbox.innerHTML + "Enter a number <br>";
      console.log("Enter a number");
      return;
  }
  retVal = "gcd of "+ a + " and " +b + " -> "+ gcd(a, b);
  console.log(retVal);
  textbox.innerHTML = textbox.innerHTML + retVal +"<br>";
  return retVal;

};

var randStudent = function(){
  // Generates a random Student through the function.
  var textbox = document.getElementById('log');
  retVal = randomStudent();
  console.log(retVal);
  textbox.innerHTML = textbox.innerHTML + retVal + "<br>";
  return retVal;
};

// Random Fib button
var b = document.getElementById('button');
// console.log(b);
b.addEventListener('click', randFib);

// Clear Output button
document.getElementById('clear').addEventListener('click', wipes);

// Choose your own nth Fibonacci number
document.getElementById("numberB").addEventListener('click', chooseYourFib);

// Random Fib button
var randGcd = document.getElementById('randGCD');
// console.log(b);
randGcd.addEventListener('click', randGCD);

// Choose your own a and b to find the gcd.
document.getElementById("userGCD").addEventListener('click', chooseYourGCD);

//Random Student Function
document.getElementById('randStu').addEventListener('click', randStudent);
