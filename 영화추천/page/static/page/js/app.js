const app = new Vue({
    el:'#app',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        movies: [],
        genres: [],
       
    },
    methods : {	
        
        
        getMovies: function () {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/posts/')
            .then(res => res.data)
            .then(movies => {this.movies = movies})
            .then(()=> {
                this.changeGenres(this.movies, this.genres);
            })
        },
        
        getGenres: function () {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/genres/')
            .then(response => response.data)
            .then(genres => {this.genres = genres})
            
        }, 
        
        changeGenres: function(movies, genres){
            for(i = 0; i < movies.length; i++){
                for(j = 0; j < genres.length; j++){
                    if (movies[i].genres == genres[j].genre_box_id) {
                        movies[i].genres = genres[j].name
                    }  
                }
            }
        },
        

        
    },
    
    mounted: function() {
        this.getGenres()
        this.getMovies()
        
    },
})
