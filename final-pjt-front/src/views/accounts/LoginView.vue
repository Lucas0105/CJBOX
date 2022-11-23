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
          <div id="naver_id_login" style="display: none;">
        </div>
        
        <!-- <div id="signin_button"></div> -->
        <img src="@/assets/kakao-icon.png" width="30%" alt="" @click="kakaoLoginBtn">
        <img src="@/assets/naver-icon.png" width="25%" height="50%" alt="" @click="naverBtn">
        <img src="@/assets/google_icon.png" width="25%" alt="" @click="googleBtn">
      </div>
    </form>
  </div>
</template>

<script src="https://unpkg.com/jwt-decode/build/jwt-decode.js"></script>
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
  mounted(){
    const naver_id_login = new window.naver_id_login(process.env.VUE_APP_NAVER_ID, "http://localhost:8080/accounts/login");

    if (naver_id_login.getAccessToken()){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/accounts/naver/${naver_id_login.getAccessToken()}/`,
      })
      .then((res) => {
        console.log(res.data.email)
        this.username = res.data.username
        this.password = '1111'
        this.logIn()
      })
      .catch((err) => {
        console.log(err)
      })
    } else {
      const naver_id_login = new window.naver_id_login(process.env.VUE_APP_NAVER_ID, "http://localhost:8080/accounts/login");
      const state = naver_id_login.getUniqState();
      naver_id_login.setButton("green", 1, 40); // 버튼 설정
      naver_id_login.setState(state);
      // naver_id_login.setPopup(); // popup 설정을 위한 코드
      naver_id_login.init_naver_id_login();
    }     
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
      naverBtn() {
        const btnNaverLogin = document.getElementById("naver_id_login").firstChild;
        btnNaverLogin.click();
      },
      googleBtn(){
        console.log(window.google.accounts.id)
        window.google.accounts.id.initialize({
              client_id: "141965149329-ru5fo46aq9jstof66os3p745susngarq.apps.googleusercontent.com",
              callback: this.handleCredentialResponse
          });
        window.google.accounts.id.prompt();
      },
      handleCredentialResponse (response) {
          // decodeJwtResponse() is a custom function defined by you
          // to decode the credential response.

          const profile = jwt_decode(response.credential);
          
          console.log(profile)
          const payload = {
                  "username": profile.email,
                  "nickname": profile.given_name,
                  "my_image": profile.picture,
                  "intro": null,
                  "password": '1111',
                }
          axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/accounts/google/',
              data: payload
            })
            .then(() => {
              this.username = profile.email,
              this.password = '1111'
              this.logIn()
            })
            .catch((err) => {
              console.log(err)
            })
      }
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
  cursor: pointer;
}

.naver_id_login img{
  border-radius: 10%;
}

</style>