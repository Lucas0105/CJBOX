<template>
  <div class="detail-page">
    <TheDetail
    :movie="movie"
    />
    <TheReview
    />
    
  </div>
</template>

<script>
import TheDetail from '@/components/TheDetail'
import TheReview from '@/components/TheReview'

export default {
    name:'DetailView',
    components:{
      TheDetail,
      TheReview
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
}

</style>