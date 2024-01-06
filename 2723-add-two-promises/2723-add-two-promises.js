/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return new Promise( async (res,rej)=>{
const resp= await Promise.all([promise1,promise2]) //[output1,output2]
res(resp[0]+resp[1])
    })
    
    
};

