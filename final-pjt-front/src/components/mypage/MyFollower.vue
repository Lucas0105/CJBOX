<template>
  <div class="col-6" style="border:solid 1px red">
    <div class="d-flex" style="border:solid 1px yellow">    
    {{ follower.nickname }}
    {{ follower.intro }}
    <img :src="userImage" alt="">
  </div>
</div>
</template>

<script>
export default {
    name:'MyFollower',
    props:{
        follower:Object
    },
    computed:{
        userImage(){
        if (this.follower.my_image){
          const index = this.follower.my_image.indexOf("k.kakaocdn.net")
          const naver_index = this.follower.my_image.indexOf("ssl.pstatic.net")
          const google_index = this.follower.my_image.indexOf("lh3.googleusercontent.com")

          if (index !== -1){
            return 'http://' + this.follower.my_image.slice(index,)
          } else if(naver_index !== -1){
            return 'http://' + this.follower.my_image.slice(naver_index,)
          } else if(google_index !== -1){
            return 'https://' + this.follower.my_image.slice(google_index,)
          } else {
            return "http://127.0.0.1:8000" + this.follower.my_image
          }
        } else{
          return null
        }
      }
    }
}
</script>

<style>

</style>