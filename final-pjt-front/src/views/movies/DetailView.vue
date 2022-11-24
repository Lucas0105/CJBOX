<template>
  <div class="detail-page">
    <MovieInfo
    :movie="movie"
    />
    <div style="color:white">
      <BannerList
      :movies="similar"
      :detail="true"
      />
    </div>
    <TheReview
    :movie="movie"
    :reviews="reviews"
    :page="currentPage"

    />
    <!-- pagination -->
      <div class="overflow-auto">
        <div class="mt-3">
          <b-pagination
            v-model="currentPage"
            pills
            :total-rows="totalPage"
            :per-page="perPage"
            first-number
            @input="getReviews"
          ></b-pagination>
        </div>
    </div>
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
          currentPage:1,
          perPage:1        
        }
      },
    computed:{
      movie(){
        return this.$store.getters['movie/detailMovie']
      },
      reviews(){
        return this.$store.getters['movie/getReview']?.reviews
      }, 
      totalPage(){
        return this.$store.getters['movie/getReview']?.page_cnt
      },
      isCreate(){
        return this.$store.getters['user/isCreate']
      },
      similar(){
        return this.$store.getters['movie/getSimilar']
      }
    },
    methods:{ 
      CheckUpdate(){
        this.$store.commit('user/CHANGE_REVIEW', null)
      },
      getMovieDetail() {
        return this.$store.dispatch('movie/getMovieDetail', this.$route.params.id)
      },
      getReviews() {
        const payload = {
          page: this.currentPage,
          movie_id : this.$route.params.id
        }
        console.log(payload)
        this.$store.dispatch('movie/getReviews', payload)
      }
    },
    created(){
      this.getMovieDetail()
      this.getReviews()
      this.CheckUpdate()
      this.$store.dispatch('movie/getSimilar', this.$route.params.id)
    },
    watch:{
      isCreate: {
        handler: 'getReviews'
      }
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

ul{
  justify-content: center;
}
</style>