import axios from "axios";

// const request = axios.create({
//     baseURL : 'http://127.0.0.1:8000/'
// })

const request = axios.create({
    baseURL : 'http://8.130.99.147:8000/'
})

request.postData = function(url, data){
    return this.post(url, data, {
        headers:{
            'Content-Type': 'application/json'
        }
    })
}
export default request