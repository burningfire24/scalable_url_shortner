// function outer(){
//     let i=0
//     function inner(){
//         setInterval(function(){ 
//             console.log(i); 
//             i++;
//         },i*1000);
//     }
//     return inner;
// }

// console.log("hello");
// outer()();


function getRedisClient(key) { //qFSvAAdJ7
    const hash = key.split('');
    console.log(hash);
    
    // return redisClients[hash % redisClients.length];
}

console.log(getRedisClient('qFSvAAdJ7'));
