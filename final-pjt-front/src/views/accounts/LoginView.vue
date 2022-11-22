<template>
  <div class="login-page">
    <form @submit.prevent="logIn" class="login-box d-flex flex-column mx-auto ">
      <p>로그인</p>
      <input type="text" placeholder="아이디" id="user-id" class="mx-auto mb-3" v-model="username">
      <input type="password" placeholder="비밀번호" id="user-pwd" class="mx-auto mb-3" v-model="password">
      <b-button type="submit" class="login-btn mx-auto mb-4">로그인</b-button>
      <div class="bottom-box d-flex justify-content-between mx-auto">
        <p>아이디 · 비밀번호 찾기</p>
        <p>회원가입</p>
      </div>
      <div class="social-container">
        <img src="@/assets/kakao-icon.png" width="30%" alt="" @click="kakaoLoginBtn">
        <img src="@/assets/kakao-icon.png" width="30%" alt="" @click="kakaoLoginBtn">
        <img src="@/assets/kakao-icon.png" width="30%" alt="" @click="kakaoLoginBtn">
      </div>
    </form>
  </div>
</template>
<script>
import axios from 'axios'

export default {
    name:'LoginView',
    data() {
      return{
        username : null,
        password : null,
      }
    },  
    computed:{

  },
    methods:{
      
      logIn(){
        // console.log(this.username, this.password)
        const username = this.username
        const password = this.password
        const payload = {
          username, 
          password
        }
        this.$store.dispatch('user/logIn', payload)
      },
      kakaoLoginBtn() {
        const thisRef = this
        console.log(window.Kakao.Auth)
        console.log(window.Kakao.Auth.getAccessToken())
        // 카카오 로그인 재시도 시 accessToken 해제
            // window.Kakao.API.request({
            //   url: '/v1/user/unlink',
            //   success: function (response) {
            //     console.log('data1')
            //     console.log(response)
            //   },
            //   fail: function (error) {
            //     console.log(error)
            //   },
            // })
            // window.Kakao.Auth.setAccessToken(undefined)

        window.Kakao.Auth.login({
          success (){
            window.Kakao.API.request({
              url: '/v2/user/me',
              success: async function (response) {
                const payload = {
                  "username": response.kakao_account.email,
                  "email":response.kakao_account.email,
                  "nickname": response.properties.nickname,
                  "my_image": response.properties.thumbnail_image,
                  "intro": null,
                  "password": '1111',
                }

                axios({
                  method: 'post',
                  url: 'http://127.0.0.1:8000/accounts/kakao/',
                  data: payload
                })
                .then(() => {
                  thisRef.username = payload['username']
                  thisRef.password = payload['password']
                  thisRef.logIn()
                })

              },
              fail: function (error) {
                console.log(error)
              },
            })
          },
          fail: function (error) {
            console.log(error)
          },
        })
      },
  }
}
</script>

<style scoped>
.login-page{
  position: relative;
  top: -80px;
  background-image : url('@/assets/login-bg.jpg');
  background-repeat: no-repeat;
  background-size: contain;
  background-size: cover ;
  height:100vh;
  text-align: center;
  display: flex;
  align-items: center;
  justify-items: center;  
}
.login-box{
  width: 30%;
  padding-top:70px;
  padding-bottom:70px;
  background-color:rgba(217,217,217,0.4);
  z-index: 1;
}
p{
  color:aliceblue;
}

#user-id, #user-pwd{
  background-color: white;
  width:70%;
}
input::placeholder{
  color:#17223b;
  /* opacity: .8; */
  font-weight: bold;

}
input{
  padding-left:10px;
  height:45px;
  border:0;
  border-radius: 4px;
  opacity: 0.4;
  font-weight: bold;
}
.login-box>p{
  font-size:20px
}
.login-btn{
  background-color: #ff6768 !important;
  width: 70%;
  height:45px;
  border:0;
}
.bottom-box{
  width: 70%;
}
.social-container{
  display: flex;
  justify-content: center;
  margin: auto;
  width: 50%;
}
.social-container img{
  margin: 0 10%;
}

</style>