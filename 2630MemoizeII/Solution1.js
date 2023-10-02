/**
 * @param {Function} fn
 */
function memoize(fn) {
    let cacheObject = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (key in cacheObject) {
            return cacheObject[key];
        }else{
            cacheObject.set(key,fn(...args));
            return cacheObject[key];
        }
    }
}