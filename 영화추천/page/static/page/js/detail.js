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
            URL = `/posts/v1/posts/${movie_id}/`
            axios.get(URL)
                .then(res => res.data)
                .then(movies => {this.movies = movies})




        },

        getGenres: function () {
            axios.get('/posts/v1/genres/')
                .then(response => response.data)
                .then(genres => {this.genres = genres})
                console.log('getGenres')

        },

        getActors: function() {
            axios.get('/posts/v1/actors/')
                .then(response => response.data)
                .then(actors => {this.actors = actors})
                console.log('getActors')
        },


    },

    mounted: function() {
        this.getActors()
        this.getGenres()
        this.getMovies()

    },
})
