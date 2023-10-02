/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    if (functions.length === 0) {
        return (x) => {return x};
    }

    return functions.reduceRight((prevFn,nextFn)=>{
        return (x) => {return nextFn(prevFn(x))}
    })
};