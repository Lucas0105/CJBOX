<template>
  <div class="genre-view">
    {{ $route.params.category}}
    <h1>genre</h1>
    <p>추천영화</p>
    <!-- <BannerList/> -->
    <div class="movie-body-box">
      <p>인기영화</p>
      <BodyList
        :movies="genreMovie"
        @current-page="getGenreMovie"
        :rows="rows"
        :currentPage="currentPage"
      />
    </div>
    
  </div>
</template>

<script>
// import BannerList from '@/components/BannerList'
import BodyList from '@/components/BodyList'

export default {
    name:'GenreView',
    data(){
      return{
        genre_name : this.$route.params.category,
        rows: 10,
        currentPage: 1,
      }
    },
    components:{
      // BannerList,
      BodyList
    },
    computed:{
      genreMovie(){
        return this.$store.state.movie.genreMovieData
      }
    },
    methods:{
      getGenreMovie(page){
        this.currentPage = page
        const genre_name = this.genre_name 
        const genre_page = page
        console.log(genre_page)
        
        const payload = {
          genre_name, genre_page
        }
        console.log(payload)
        return this.$store.dispatch('movie/getGenreMovie', payload)
      },

    },
    created(){
      this.getGenreMovie()
    },
    beforeRouteUpdate(to, from, next){
      this.genre_name = to.params.category
      this.getGenreMovie()
      next()
    }
}
</script>

<style>
.genre-view{
  height: 100%;
}
</style>