const main = new Vue({
    el:'#main',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        movies: [],

    },
    methods : {

        getMovies: function () {
            axios.get('/posts/v1/posts/')
            .then(res => res.data)
            .then(movies => {this.movies = movies})

        },

    },

    mounted: function() {
        this.getMovies()

    },
})
