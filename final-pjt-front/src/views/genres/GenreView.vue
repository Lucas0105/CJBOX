<template>
  <div>
    <h1>genre</h1>
    <p>추천영화</p>
    <BannerList/>
    <p>인기영화</p>
    <BodyList/>

  </div>
</template>

<script>
import BannerList from '@/components/BannerList'
import BodyList from '@/components/BodyList'

export default {
    name:'GenreView',
    components:{
      BannerList,
      BodyList
    }
}
</script>

<style>

</style>