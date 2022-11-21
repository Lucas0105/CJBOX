<template>
  <div class="detail-page">
    <MovieInfo
    :movie="movie"
    />
    <hr style="color:white">
    <div style="color:white" title="추후 수정">
      비슷한 영화 추천
      <BannerList/>
    </div>
    <TheReview
    :movie="movie"
    />

  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import TheReview from '@/components/TheReview'
import BannerList from '@/components/BannerList'

export default {
    name:'DetailView',
    components:{
      MovieInfo,
      TheReview,
      BannerList
    },
    data(){
        return{
        }
      },
    computed:{
      movie(){
        return this.$store.state.movie.movieDetail
      }
    },
    methods:{
      getMovieDetail() {
        return this.$store.dispatch('movie/getMovieDetail', this.$route.params.id)
      },
    },
    created(){
      this.getMovieDetail()
    },

}
</script>

<style scoped>
.detail-page{
  display: flex;
  position: relative;
  top: -80px;
  background-color: #17223b;
  flex-direction: column;
}

</style>