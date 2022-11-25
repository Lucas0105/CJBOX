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
      <div class="name-box mx-auto" >
        <span style="font-weight:bold">{{userInfo.user.nickname}}</span>
      </div>
      <div class="intro-box">
          <span>{{userInfo.user.intro}}</span>
      </div>
      <div class="d-flex justify-content-evenly mt-2">
        <div v-for="(genre, index) in userInfo.genres" :key="index">
          <router-link :to="{ name: 'genre', params: {category: genre.genre.name} }">
            <small><b-button pill class="genre_btn">{{genre.genre.name}}</b-button></small>
          </router-link>
        </div>
      </div>
      <div v-if="loginUserName!==userInfo.user.nickname" class="follow-btn-box d-flex">
        <b-button class="follow-btn mx-auto"  @click="follow" v-if="!followData.is_follow">Follow</b-button>
        <b-button class="follow-btn mx-auto"  @click="follow" v-else >UnFollow</b-button>
      </div>
      <div class="follow mx-auto d-flex flex-column">
        <div><span>Following:</span> {{followData.following_cnt}}</div>
        <div><span>Follower:</span> {{followData.followed_cnt}}</div>
      </div>

      <div class="svg-item">
        <svg width="100%" height="100%" viewBox="0 0 40 40" class="donut">
          <circle class="donut-hole" cx="20" cy="20" r="15.91549430918954" fill="#fff"></circle>
          <circle class="donut-ring" cx="20" cy="20" r="15.91549430918954" fill="transparent" stroke-width="3.5"></circle>
          <circle class="donut-segment" cx="20" cy="20" r="15.91549430918954" fill="transparent" stroke-width="3.5" :stroke-dasharray="sentiment+' '+ (100-sentiment)" stroke-dashoffset="25"></circle>
          <g class="donut-text">

            <text y="50%" transform="translate(0, 2)">
              <tspan x="50%" text-anchor="middle" class="donut-percent">{{ sentiment }}</tspan>   
            </text>
          </g>
        </svg>
        <p>리뷰 감성 평가</p>
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
      sentiment(){
        return this.$store.state.user.userInfo.reviews_avg
      }
    },
    methods:{
      follow(){
        this.$store.dispatch('user/follow', this.userInfo.user.nickname)
      }
    },
    beforeRouteUpdate(to) {
      console.log('teststotototo')
      console.log(to)
    }
}
</script>

<style scoped>
.background{
  border:solid 1px orange;
  min-height: 25% ;
  background-color: orange;
  position: relative;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  border-top-left-radius: 10px;

}
.img-box{
  position: absolute;
  top:17%;
  left:37%;
  
}
.profile-box{
  min-height: 90%;
  width: 23%;
  color: aliceblue;
  border-radius: 10px;
  background-color: rgba(0,0,0,0.4);
  position: relative;
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
  margin-top:17%
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
  position: absolute;
  bottom: 29%;
  left: 40%;
}
.follow-btn-box{
  margin-top:13%;
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


.svg-item {
  width: 200px;
  height: 200px;
  font-size: 16px;
  margin: auto;
  position: absolute;
  bottom: 5%;
  left: 25%;
}

.svg-item p {
  text-align: center;
}

.donut-ring {
  stroke: #EBEBEB;
}

.donut-segment {
  animation: donut-chart-fill 1s reverse ease-in;
  transform-origin: center;
  stroke: #FF6200;
}

.donut-text {
  font-family: Arial, Helvetica, sans-serif;
  fill: #FF6200;
}

.donut-label {
  font-size: 0.28em;
  font-weight: 700;
  line-height: 1;
  fill: #000;
  transform: translateY(0.25em);    
}

.donut-percent {
  font-size: 0.5em;
  fill: #FF6200;
  line-height: 1;
  transform: translateY(0.5em);
}
</style>