<template>
  <div class="col-6 h-100 mb-4" style=" ">
    <div class="d-flex" style="background-color:snow;  border-radius:10px; width:100%; height:7em;   color:black" @click="goToUserPage(follower.nickname)">
        <div class="d-flex img-box mx-auto" style="width:30%">
            <div class="r-box mx-auto my-auto">
                <img class="r-profile" :src="userImage" alt="userImg">
            </div>
        </div>
        <div class="d-flex flex-column my-auto" style="color:black; width:80%; height:auto">
                <h4>
                    {{ follower.nickname }}
                </h4>
                <div class="p-2" style="background-color:#E2E2E2; width:80%; height:3em; border-radius:10px" >
                   <span>{{ follower.intro }}</span>
                </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'MyFollower',
    data(){
      return{
        
      }
    },
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
    },
    methods:{
      goToUserPage(nickname){
        this.$router.push({name: 'mypage', params: {nickname: nickname}})
      }
      
    }
}
</script>

<style>

</style>