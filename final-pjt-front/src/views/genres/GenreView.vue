<template>
  <div>
    {{ $route.params.category}}
    <h1>genre</h1>
    <p>추천영화</p>
    <BannerList/>
    <p>인기영화</p>
    <BodyList
      :movies="genreMovie"
      @current-page="getGenreMovie"
    />
    
  </div>
</template>

<script>
import BannerList from '@/components/BannerList'
import BodyList from '@/components/BodyList'

export default {
    name:'GenreView',
    data(){
      return{
        genre_name : this.$route.params.category

      }
    },
    components:{
      BannerList,
      BodyList
    },
    computed:{
      genreMovie(){
        return this.$store.state.movie.genreMovieData
      }
    },
    methods:{
      getGenreMovie(page){
        const genre_name = this.genre_name 
        const payload = {
          genre_name, page
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

</style>