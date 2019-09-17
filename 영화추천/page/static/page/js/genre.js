const genre = new Vue({
    el:'#genre',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        movies: [],
        genres: [],
        genreMovies: [],
    },
    methods : {
        
        getMovies: function () {
            const genre_id = document.querySelector( 'nooooooooooryuc' ).getAttribute( 'id' )
            
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/posts/')
            .then(res => res.data)
            .then(movies => {this.movies = movies})
            .then(() => {
                this.getgenreMovies(this.movies, genre_id, this.genreMovies);
            })
            .then(()=> {
                this.changeGenres(this.movies, this.genres);
            })
        },
        
        getgenreMovies: function(movies, genre_id, genreMovies) {
            for(i = 0; i< movies.length; i++){
                if (genre_id == movies[i].genres) {
                    genreMovies.push(movies[i])
                }
            }
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
