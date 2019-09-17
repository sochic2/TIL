const detail = new Vue({
    el:'#detail',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        
        movies: "",
        genres: [],
        actors: [],
       
    },
    methods : {
        
        getMovies: function () {
            const movie_id = document.querySelector( 'nooooooooooryuc' ).getAttribute( 'id' )
            URL = `https://django-project-rngus3050.c9users.io/posts/v1/posts/${movie_id}/`
            axios.get(URL)
                .then(res => res.data)
                .then(movies => {this.movies = movies})
                // .then(()=> {
                //     this.changeGenres(this.movies, this.genres);
                // })
                // .then(()=> {
                //     this.changeActors(this.movies, this.actors);
                // })
                
        
            
            
        },
        
        getGenres: function () {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/genres/')
                .then(response => response.data)
                .then(genres => {this.genres = genres})
                console.log('getGenres')
            
        }, 
        
        getActors: function() {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/actors/')
                .then(response => response.data)
                .then(actors => {this.actors = actors})
                console.log('getActors')
        },
        
        // changeGenres: function(movies, genres){
        //     for(j = 0; j < genres.length; j++){
        //         if (movies.genres == genres[j].genre_box_id) {
        //             movies.genres = genres[j].name
        //         }  
        //     }
            
        // },
        
        // changeActors: function(movies, actors){
        //     for(j = 0; j < actors.length; j++){
        //         if (movies.actor_1 == actors[j].actor_id) {
        //             movies.actor_1 = actors[j].actor_name
        //         }else if (movies.actor_2 == actors[j].actor_id) {
        //             movies.actor_2 = actors[j].actor_name
        //         }else if (movies.actor_3 == actors[j].actor_id) {
        //             movies.actor_3 = actors[j].actor_name
        //         }
                
        //     }
            
        // },
        

        
    },
    
    mounted: function() {
        this.getActors()
        this.getGenres()
        this.getMovies()
        
    },
})
