<template>
  <div class="main-view">  
    <div id="movie-banner-box">
      <div class="movie-banner">
        <p>추천영화</p>
        <!-- <BannerList/> -->
        <p>인기영화</p>
        <!-- <BannerList/> -->
      </div>
    </div>
    <div class="movie-body-box">
      <p>최신영화</p>
      <BodyList
        :movies="recentMovie"
        @current-page="getRecentMovie"
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
    name:'MovieView',
    components:{
      // BannerList,
      BodyList
    },
    data(){
      return{
        rows: 10,
        currentPage: 1,
      }
    },
    computed:{
      recentMovie(){
        return this.$store.state.movie.recentMovieData
      },
      popularMovie(){
        return this.$store.state.movie.popularMovieData
      }
    },
    methods:{
      getRecentMovie(page){
        this.currentPage = page
        return this.$store.dispatch('movie/getRecentMovie', page)
      },
      getPopularMovie(){
        return this.$store.dispatch('movie/getPopularMovie')
      },
    },
    created(){
      this.getRecentMovie()
      this.getPopularMovie()            
    }
    


}
</script>

<style>
#movie-banner-box{
  background-color: #17223b;
  position: relative;
  top: -80px;
  background-image:  url("@/assets/comdey1.gif");
  background-size: cover;
  background-repeat: no-repeat;
  height: 100vh;
  width : 100%
  }

.movie-body-box{
  background-color: #17223b;
  position: relative;
  top: -80px;
}
.movie-banner{
  padding-top:50px;

}
.main-view{
  height: 100%;
}
</style>