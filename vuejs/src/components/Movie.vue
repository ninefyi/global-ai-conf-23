<template>
    <div>
        <input type="text" v-model="query" />
        <button @click="searchMovies">Search</button>
    </div>
    <div>
        <div v-if="loading">Loading...</div>
        <div v-else>
            <div v-for="movie in movies">
                <MovieItem :title="movie.title" :plot="movie.plot" :poster="movie.poster" :year="movie.year" :score="movie.score"  />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import MovieItem from './MovieItem.vue';

export default {
    components: {
        MovieItem
    },
    data() {
        return {
            movies: [],
            loading: true,
            query: ''
        };
    },
    mounted() {
      this.loading = false;
    },
    methods: {
        searchMovies() {
            this.loading = true;
            axios.get(`http://localhost:8000/search?query=${this.query}`)
                .then(response => {
                    this.movies = response.data.results;
                    this.loading = false;
                })
                .catch(error => {
                    console.error(error);
                    this.loading = false;
                });
        }
    }
};
</script>
