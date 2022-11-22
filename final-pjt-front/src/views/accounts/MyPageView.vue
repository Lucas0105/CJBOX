<template>
  <div class="my-page">
    <div class="mypage-wrapper mx-auto">
      <h1>mypage</h1>
      <TheProfile/>
      <MyList/>
    </div>
  </div>
</template>

<script>
import MyList from '@/components/MyList'
import TheProfile from '@/components/TheProfile'

export default {
    name:'MyPageView',
    components:{
      MyList,
      TheProfile
    }
}
</script>

<style scoped>
.my-page{
  position: relative;
  top: -80px;
  height:100vh;
  display: flex;
}
.mypage-wrapper{
  width:50%;
  border: solid 1px black;
  margin-top:80px;
}
</style>