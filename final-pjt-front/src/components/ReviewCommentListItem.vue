<template>
  <div class="d-flex">
    <div >
      <div class="d-flex img-box">
        <div class="r-box" style="background-color:white;   ">
          <img class="r-profile" :src="userImage" alt="userImg">
        </div>
      </div>
      <p>{{ comment.user.nickname}}</p>
    </div>
    <div>
      <p>{{comment.content}}</p>
      <p class="time">{{ comment.created_at}}</p>
    </div>

  </div>
</template>

<script>
export default {
    name:'ReviewCommentListItem',
    props:{
      comment:Object
    },
    data() {
      return{
      }
    },
    computed:{
      userImage(){
        if (this.comment.user.my_image){
          const index = this.comment.user.my_image.indexOf("k.kakaocdn.net")
          const naver_index = this.comment.user.my_image.indexOf("ssl.pstatic.net")
          const google_index = this.comment.user.my_image.indexOf("lh3.googleusercontent.com")

          if (index !== -1){
            return 'http://' + this.comment.user.my_image.slice(index,)
          } else if(naver_index !== -1){
            return 'http://' + this.comment.user.my_image.slice(naver_index,)
          } else if(google_index !== -1){
            return 'https://' + this.comment.user.my_image.slice(google_index,)
          } else {
            return "http://127.0.0.1:8000" + this.comment.user.my_image
          }
        } else{
          return null
        }
      }
    },   
}
</script>

<style scoped>
.r-box{
  width: 50px;
  height: 50px; 
  border-radius: 100%;
  overflow: hidden;
}

.r-profile{
  position: relative;
  width: 50px;
  height: 50px;
  border-radius: 50%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.time{
  color:gray;
  font-size:14px;
}

</style>