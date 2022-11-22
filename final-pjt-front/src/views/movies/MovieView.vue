<template>
  <div class="main-view">  
    <div id="movie-banner-box" :style="{'background-image': 'url('+backdrop_path+')'}">
      <div class="content-container">
        <h1>
          {{ background_title }}
        </h1>
        <div class="overview_container">
          {{ background_overview }}
        </div>
        <button @click="toDetail" class="btn btn-warning mt-3 px-5 py-2">
          <span class="fs-5">더보기</span>
        </button>
      </div>
    </div>
    <div class="movie-body-box pt-5">
      <div class="movie-banner">
        <div class="banner-container">
          <p class="fs-1 text-white">추천영화</p>
          <BannerList :movies="recommend"/>
          <p class="fs-1 text-white">인기영화</p>
          <BannerList :movies="popularMovie"/>
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
        backdrop_path: null,
        background_id: null,
        background_title: null,
        background_overview: null,
      }
    },
    computed:{
      recentMovie(){
        return this.$store.state.movie.recentMovieData
      },
      popularMovie(){
        return this.$store.state.user.popularMovieData
      },
      recommend(){
        return this.$store.state.user.recommend
      }
    },
    methods:{
      getRecentMovie(page){
        this.currentPage = page
        return this.$store.dispatch('movie/getRecentMovie', page)
      },
      toDetail() {
        this.$router.push({name:'detail', params:{id: this.background_id}})
      }
    },
    created(){
      this.getRecentMovie()   
      this.$store.dispatch('user/backDrop')
      this.$store.dispatch('user/recommend')
      this.$store.dispatch('user/getPopularMovie')
    
      const movie = this.$store.state.user.background_movie
      this.background_id = movie.id
      this.backdrop_path = movie.backdrop_path
      this.background_title = movie.title
      this.background_overview = movie.overview

    },
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

.content-container{
  position: absolute;
  top: 35%;
  left: 10%;
  color: rgb(247, 88, 88);
}

.overview_container{
  color: rgb(255, 255, 255);
  width: 40%;
}

</style>