<template>
  <div class="detail-page">
    <MovieInfo
    :movie="movie"
    />
    <div style="color:white" title="추후 수정">
      비슷한 영화 추천
      <BannerList/>
    </div>
    <TheReview
    :movie="movie"
    :reviews="reviews"
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
          page:1
        }
      },
    computed:{
      movie(){
        return this.$store.getters['movie/detailMovie']
      },
      reviews(){
        return this.$store.getters['movie/getReview']
      }, 
      isCreate(){
        return this.$store.getters['user/isCreate']
      }
    },
    methods:{ 
      getMovieDetail() {
        return this.$store.dispatch('movie/getMovieDetail', this.$route.params.id)
      },
      getReviews() {
        const payload = {
          page: this.page,
          movie_id : this.$route.params.id
        }
        console.log(payload)
        this.$store.dispatch('movie/getReviews', payload)
      }
    },
    created(){
      this.getMovieDetail()
      this.getReviews()
    },
    watch:{
      isCreate: {
        handler: 'getReviews'
      }
    }
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