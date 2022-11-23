<template>
  <div class="profile-box">
    <div class="background">
    </div>
    <div class="d-flex img-box mx-auto">
      <div class="r-box" style="background-color:white;   ">
        <img class="r-profile" :src="userImage" alt="userImg">
      </div>
    </div>
    <div class="d-flex flex-column intro-out-box">
      <div class="name-box">
        <h3 style="font-weight:bold">{{userInfo.user.nickname}}</h3>
      </div>
      <div class="intro-box">
        <div>
          <span>{{userInfo.user.intro}}</span>
        </div>
      </div>
      <div class="favorit" v-for="(genre, index) in userInfo.genres" :key="index">
        <small><b-button>{{genre.genre.name}}</b-button></small>
        
      </div>
      <div class="follow mx-auto d-flex flex-column">
        <div><span>Following:</span> {{userInfo.following_cnt}}</div>
        <div><span>Followers:</span> {{userInfo.followed_cnt}}</div>
      </div>
        <b-button class="follow-btn mx-auto" v-if="isFollow" @click="follow">Follow</b-button>
        <b-button class="follow-btn mx-auto" v-else >Following</b-button>
  </div>
</div>
</template>

<script>
export default {
    name:'TheProfile',
    props:{
      userInfo:Object
    },
    data(){
      return{
        isFollow : true
      }
    },
    computed:{
      userImage(){
        if (this.userInfo.user.my_image){
          const index = this.userInfo.user.my_image.indexOf("k.kakaocdn.net")
          const naver_index = this.userInfo.user.my_image.indexOf("ssl.pstatic.net")
          
          if (index !== -1){
            return 'http://' + this.userInfo.user.my_image.slice(index,)
          } else if(naver_index !== -1){
            return 'http://' + this.userInfo.user.my_image.slice(naver_index,)
          } else {
            return "http://127.0.0.1:8000" + this.userInfo.user.my_image
          }
        } else{
          return null
        }
      }
    },
    methods:{
      follow(){
        this.$store.dispatch('user/follow', this.userInfo.user.nickname)
      }
    }
}
</script>

<style scoped>
.background{
  border:solid 1px orange;
  min-height: 33% ;
  background-color: orange;
  position: relative;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  border-top-left-radius: 10px;

}
.img-box{
  position: absolute;
  top:32%;
  left:12%;
}
.profile-box{
  min-height: 90%;
  width: 25%;
  color: aliceblue;
  text-align: center;
  border-radius: 10px;
  background-color: rgba(0,0,0,0.4);
}

.r-box{
  width: 7em;
  height: 7em; 
  border-radius: 100%;
  overflow: hidden;
}

.r-profile{
  position: relative;
  width: 7em;
  height: 7em;
  border-radius: 100%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.intro-out-box{
  margin-top:20%
}

.follow{
  /* margin-top:40% */
}

.follow-btn{
  width:90%;
  background-color: #ff6768;
  border:none
}
.follow-btn:hover{
  background-color: #263859;

}
</style>