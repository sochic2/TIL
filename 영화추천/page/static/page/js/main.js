const main = new Vue({
    el:'#main',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        movies: [],
       
    },
    methods : {
        
        getMovies: function () {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/posts/')
            .then(res => res.data)
            .then(movies => {this.movies = movies})
            
        },
      
    },
    
    mounted: function() {
        this.getMovies()
        
    },
})
