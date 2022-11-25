<template>
  <div class="d-flex comment-item justify-content-between">
    <div class="d-flex-col mx-2 my-auto" style="text-align:center">
      <div class="d-flex img-box">
        <div class="r-box" style="background-color:white;   ">
          <img class="r-profile" :src="userImage" alt="userImg">
        </div>
      </div>
      <p style="margin-bottom:0">{{ comment.user.nickname}}</p>
    </div>
    <div style="width:80%" class="d-flex flex-column justify-content-between">
      <p style="word-wrap:break-word; width:100%">{{comment.content}}</p>
      <p class="time" style="margin-bottom:1px; width:100%">{{ comment.created_at}}</p>
    </div>
    <div style="text-align:center" class="d-flex align-items-end" v-if="loginUserName===comment.user.nickname">
      <div class="m-2" @click="commentDelete" style="cursor:pointer; ">삭제</div>
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
      loginUserName(){
        return this.$store.state.user.login_user.nickname
      },
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
    methods:{
      commentDelete(){
        this.$store.dispatch('user/commentDelete', this.comment.id)
      }
    }
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

  .comment-item{
    background-color: snow;
    border-radius: 4px;

  }

</style>