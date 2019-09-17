const base = new Vue({
    el:'#base',
    delimiters: [`${'[['}`, `${']]'}`],
    data: {
        genres: [],
       
    },
    methods : {
        getGenre: function () {
            axios.get('https://django-project-rngus3050.c9users.io/posts/v1/genres/')
            .then(response => response.data)
            .then(genres => {this.genres = genres})
            
        }, 
    },
    
    mounted: function() {
        this.getGenre()
        
    },
})
