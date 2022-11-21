<template>
  <div class="main-view">  
    <div id="movie-banner-box" :style="{'background-image': 'url('+backgroundImg+')'}">
      
    </div>
    <div class="movie-body-box pt-5">
      <div class="movie-banner">
        <div class="banner-container">
          <p class="fs-1 text-white">추천영화</p>
          <BannerList/>
          <p class="fs-1 text-white">인기영화</p>
          <BannerList/>
        </div>
      </div>
      <p class="text-center fs-1 text-white mt-5">최신영화</p>
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
import BannerList from '@/components/BannerList'
import BodyList from '@/components/BodyList'


export default {
    name:'MovieView',
    components:{
      BannerList,
      BodyList
    },
    data(){
      return{
        rows: 100,
        currentPage: 1,
      }
    },
    computed:{
      recentMovie(){
        return this.$store.state.movie.recentMovieData
      },
      popularMovie(){
        return this.$store.state.movie.popularMovieData
      },
      backgroundImg(){
        return this.$store.state.user.background
      },
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
    },
    beforeCreate(){
      this.$store.dispatch('user/backDrop')
      this.$store.dispatch('user/recommend')
    }
    


}
</script>

<style>
.swiper-container{
  height: 40vh !important;
}

#movie-banner-box{
  background-color: #17223b;
  position: relative;
  top: -80px;
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
  opacity: 0.8;
  width: 100%;
}

.main-view{
  height: 100%;
}
</style>