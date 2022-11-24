<template>
  <div class="genre-view">
    <div class="top-category">
      <h1 style="margin-left:11%">{{ $route.params.category}}</h1>
    </div>
    <!-- <BannerList/> -->
    <div class="movie-body-box">
      <BodyList
        :movies="genreMovie?.movies"
        @current-page="getGenreMovie"
        :rows="genrePage"
        :currentPage="currentPage"
        :isInit="isInit"
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
        currentPage: 1,
        isInit: true,
      }
    },
    components:{
      // BannerList,
      BodyList
    },
    computed:{
      genreMovie(){
        return this.$store.state.movie?.genreMovieData
      },
      genrePage(){
        return this.$store.state.movie.genreMovieData?.page_cnt
      }
    },
    methods:{
      getGenreMovie(page){
        if (page){
          this.isInit = false
          console.log(this.isInit)
        } else {
          this.isInit = true
        } 
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
background-color: #17223b;
  position: relative;
  top: -80px;
  background-size: cover;
  background-repeat: no-repeat;
  height: 100vh;
  width : 100%}

.movie-body-box{
  background-color: #17223b;
  position: relative;
  top: -80px;
}
.top-category{
  padding-top:80px;
  color:aliceblue;
  width:100%
}
</style>