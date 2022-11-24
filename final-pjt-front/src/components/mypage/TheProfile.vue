<template>
  <div class="profile-box">
    <div class="background">
    </div>
    <div class="w-100">
    <div class="d-flex img-box mx-auto">
      <div class="r-box" style="background-color:white;   ">
        <img class="r-profile" :src="userImage" alt="userImg">
      </div>
    </div>
    </div>
    <div class="d-flex flex-column intro-out-box">
      <div class="name-box mx-auto">
        <h3 style="font-weight:bold">{{userInfo.user.nickname}}</h3>
      </div>
      <div class="intro-box">
          <span>{{userInfo.user.intro}}</span>
      </div>
      <div class="d-flex justify-content-evenly mt-4">
        <div v-for="(genre, index) in userInfo.genres" :key="index">
          <router-link :to="{ name: 'genre', params: {category: genre.genre.name} }">
            <small><b-button pill class="genre_btn">{{genre.genre.name}}</b-button></small>
          </router-link>
        </div>
      </div>
      <div class="follow mx-auto d-flex flex-column">
        <div><span>Following:</span> {{followData.following_cnt}}</div>
        <div><span>Follower:</span> {{followData.followed_cnt}}</div>
      </div>
      <div v-if="loginUserName!==userInfo.user.nickname" class="follow-btn-box d-flex">
        <b-button class="follow-btn mx-auto"  @click="follow" v-if="!followData.is_follow">Follow</b-button>
        <b-button class="follow-btn mx-auto"  @click="follow" v-else >UnFollow</b-button>
      </div>
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
      }
    },
    computed:{
      loginUserName(){
        return this.$store.state.user.login_user.nickname
      },
      userImage(){
        if (this.userInfo.user.my_image){
          const index = this.userInfo.user.my_image.indexOf("k.kakaocdn.net")
          const naver_index = this.userInfo.user.my_image.indexOf("ssl.pstatic.net")
          const google_index = this.userInfo.user.my_image.indexOf("lh3.googleusercontent.com")

          if (index !== -1){
            return 'http://' + this.userInfo.user.my_image.slice(index,)
          } else if(naver_index !== -1){
            return 'http://' + this.userInfo.user.my_image.slice(naver_index,)
          } else if(google_index !== -1){
            return 'https://' + this.userInfo.user.my_image.slice(google_index,)
          } else {
            return "http://127.0.0.1:8000" + this.userInfo.user.my_image
          }
        } else{
          return null
        }
      },
      followData(){
        return this.$store.state.user.followData
      },
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
  width: 23%;
  color: aliceblue;
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
  width: 7rem;
  height: 7rem;
  border-radius: 100%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.intro-out-box{
  margin-top:10%
}

.intro-box{
  background-color: rgba(255, 251, 251, 0.9);;
  min-height: 8vh;
  border-radius: 4px;
  color:black;
  padding:2%;
  margin:2%;
}
.follow{
  margin-top:30%
}
.follow-btn-box{
  margin-top:15%;
  width:100%
}
.follow-btn{
  width:90%;
  background-color: #ff6768;
  border:none;
}
.follow-btn:hover{
  background-color: #263859;
}

.genre_btn{
  background-color: rgb(153,50,204);
  border:none;
}

.genre_btn:hover{
  background-color: #263859;
}


</style>