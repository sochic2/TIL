const base = new Vue({
    el:'#base',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        genres: [],
       
    },
    methods : {
        getGenre: function () {
            axios.get('/posts/v1/genres/')
            .then(response => response.data)
            .then(genres => {this.genres = genres})
        }, 
    },
    
    mounted: function() {
        this.getGenre()
        
    },
})
