<template>
  <div  id="movie-body">
    <div class="movie-banner">
      <p>추천영화</p>
      <BannerList/>
      <p>인기영화</p>
      <BannerList/>
    </div>

    <p>최신영화</p>
    <BodyList/>
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
    }
}
</script>

<style>
#movie-body{
  background-color: #17223b;
  position: relative;
  top: -80px;
  background-image:  url("@/assets/comdey1.gif");
  background-size: cover;
  background-repeat: no-repeat;
  height: 100vh;}
.movie-banner{
  padding-top:100px
}
</style>