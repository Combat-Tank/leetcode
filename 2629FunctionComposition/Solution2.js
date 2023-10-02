/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return x => functions.reduceRight((comp,fn)=>fn(comp),x);
};

//function with input x
//      reduce functions with reduceRight (right 2 left)
//      callback on reduce has the function composition and "current" function as inputs
//      outputs function applied to the initial variable (can be value or function applied to value)
//      initial value for reduceRight is x