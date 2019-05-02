const axios = require('axios')
const url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts/'

axios.get(url)
    .then(res => {
        console.log(res.data.posts)
    })

const data = 
{
    "post": {
        "title": "working",
        "content": "content",
        "author": "author"
    }
}
axios.post(url, data)