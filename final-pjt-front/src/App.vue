<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg" >
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{name:'movies'}"><img src="@/assets/CJBOX_logo2-2.gif" width="60px" alt=""></router-link>
          <ul class="navbar-nav">
            <b-nav-item-dropdown class="mx-2 d-flex" text="장르" style="margin-top:2%"> 
              <b-dropdown-item v-for="(genre, index) in genres" :key="index" @click="toGenre(genre)">{{ genre }}</b-dropdown-item>
            </b-nav-item-dropdown>
            <div class="d-flex">
              <li class="nav-item mx-1 d-flex">
                <router-link class="nav-link my-auto" :to="{ name: 'search'}">
                  <b-icon icon="search" title="검색"></b-icon>
                </router-link>
              </li>
              <div class="d-flex" v-if="!isLogin">
                <li class="nav-item mx-1">
                  <router-link class="nav-link" :to="{name:'login'}"><b-icon icon="box-arrow-in-right" title="로그인"></b-icon></router-link>
                </li>
                <li class="nav-item mx-1">
                  <router-link class="nav-link " :to="{name:'signup'}"><b-icon icon="person-plus" title="회원가입"></b-icon></router-link>
                </li>
              </div>
              <div v-else class="d-flex" >
                <div class="d-flex" style="margin-right:30px;cursor:pointer; width:100%" title="마이페이지" @click="toMypage">
                  <div class="d-flex img-box">
                    <div class="box" style="background-color:white;   ">
                      <img class="profile" :src="userimage" alt="userImg">
                    </div>
                  </div>
                  <div class="d-flex" style="width:80%; font-size:calc((var(--h) / 3));">
                    <span class="username-span my-auto" style=" font-size:1em ">{{username}}</span>
                  </div>
                </div>
                <a class="nav-link my-auto" style="cursor:pointer" @click="logOut"><b-icon icon="box-arrow-right" title="로그아웃"></b-icon></a>
              </div>
            </div>
          </ul>
      </div>
    </nav>
    <router-view ></router-view>
    </div>
  
</template>

<script>

export default {
  computed:{
    genres(){
      return this.$store.state.movie.genre_list
    },
    isLogin(){
      return this.$store.getters['user/isLogin']
    },
    username(){
      return this.$store.state.user.login_user.nickname
    },
    userimage(){
      if (this.$store.state.user.login_user.my_image){
        const index = this.$store.state.user.login_user.my_image.indexOf("k.kakaocdn.net")
        const naver_index = this.$store.state.user.login_user.my_image.indexOf("ssl.pstatic.net")
        const google_index = this.$store.state.user.login_user.my_image.indexOf("lh3.googleusercontent.com")
        
        if (index !== -1){
          return 'http://' + this.$store.state.user.login_user.my_image.slice(index,)
        } else if(naver_index !== -1){
          return 'http://' + this.$store.state.user.login_user.my_image.slice(naver_index,)
        } else if(google_index !== -1){
          return 'https://' + this.$store.state.user.login_user.my_image.slice(google_index,)
        } else {
          return this.$store.state.user.login_user.my_image
        }
      } else{
        return null
      }
    }
  },
  components:{
  },
  methods:{
    logOut() {
      this.$store.dispatch('user/logOut')
    },
    toGenre(genre){
      this.$router.push({name: 'genre', params: {category: genre}})
      this.$router.go(this.$router.currentRoute)

    },
    toMypage(){
      const nickname = this.$store.state.user.login_user.nickname 
      this.$router.push({name: 'mypage', params: {nickname: nickname}})
      this.$router.go(this.$router.currentRoute)

    }
  }
}
</script>
<style>
#app{
  height:100vh;

}
.navbar{
  background-color: rgba(57, 66, 86, 0.5);
  padding: 0 !important;
  height: 80px;
  z-index: 1;
}
.nav-link{
  color:#EEEEEE !important
}
.navbar-brand{
  padding-top: 0 !important;
  padding-bottom: 0 !important
}

a:hover{
  text-decoration: none; 
}
a{
  text-decoration: none !important;
  color:aliceblue !important;
  }

input:focus{
    outline: none;
}

.dropdown-menu{
  background-color: #263859 !important;

}

.dropdown-item:hover{
  background-color: #6b778d !important;
}

.img-box{
  margin-left:4px;
  margin-right:4px
}

.box {
    width: 50px;
    height: 50px; 
    border-radius: 100%;
    overflow: hidden;
}

.profile
{
  position: relative;
  width: 50px;
  height: 50px;
  border-radius: 50%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.username-span{
  color:white; 
  margin-left:10px; 
  font-weight:bold;
}

</style>
