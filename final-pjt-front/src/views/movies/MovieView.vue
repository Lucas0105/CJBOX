<template>
  <div>  
    <div id="movie-banner-box">
      <div class="movie-banner">
        <p>추천영화</p>
        <BannerList/>
        <p>인기영화</p>
        <BannerList/>
      </div>
    </div>
    <div id="movie-body-box">
      <p>최신영화</p>
      <BodyList
        :movies="recentMovie"
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
      getRecentMovie(){
        return this.$store.dispatch('movie/getRecentMovie')
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

#movie-body-box{
  background-color: #17223b;
}
.movie-banner{
  padding-top:50px
}
</style>