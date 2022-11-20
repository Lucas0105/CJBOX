<template>
  <div class="signp-page ">
      <form @submit.prevent="signUp" class="d-flex flex-column signup-box mx-auto" >
        <p >회원가입</p>
        <input type="text" placeholder="아이디" class="mb-2 mx-auto input-style" v-model="username">
        <input type="text" placeholder="닉네임" class="mb-2 mx-auto input-style" v-model="nickName">
        <input type="text" placeholder="이메일" class="mb-2 mx-auto input-style" v-model="email">
        <input type="text" placeholder="비밀번호" class="mb-2 mx-auto input-style" v-model="password1">
        <input type="text" placeholder="비밀번호 확인" class="mb-2 mx-auto input-style" v-model="password2">
        <input type="text" placeholder=" 프로필소개" class="mb-2 mx-auto input-style" v-model="intro">
        <div class="d-flex img-box">
          <div class="box" style="border:solid 2px black; background-color:white; opacity:0.5">
            <!-- <img class="profile" src=""> -->
          </div>
          <input id="file-input" type="file" @change="getImg" ref="IMG">
        </div>

        <b-button class="signup-btn mx-auto" type="submit">회원가입</b-button>
      </form>
  </div>
</template>

<script>
export default {
    name:'SignupView',
    data(){
      return{
        username : null,
        nickName : null,
        email : null,
        password1 : null,
        password2 : null,
        intro : null,
        image : null,
      }
    },
    methods:{
      signUp() {
        const username= this.username
        const nickName= this.nickName
        const email= this.email
        const password1= this.password1
        const password2= this.password2
        const intro= this.intro
        const image= this.image

        const payload = {
          username,
          nickName,
          email,
          password1,
          password2,
          intro,
          image
        }
       
       this.$store.dispatch('user/signUp', payload)
      },
      getImg() {
        this.image = this.$refs.IMG.files[0]
        // console.log(this.image)
      }
    }
}
</script>

<style scoped>
p{
  color: aliceblue;
}

.signp-page{
  text-align:center; 
  background-image : url('@/assets/signup4.jpg');
  background-repeat: no-repeat;
  height:100vh;
  background-size: contain;
  background-size: cover ;
  position: relative;
  top: -80px;
  display: flex;
  align-items: center;
  justify-items: center;  
}
.signup-outer{
  margin-top:40px;
}
.signup-box{
  margin-top:40px;
  padding-top:20px;
  padding-bottom:20px;
  width:35%;
  background-color:rgba(217,217,217,0.4);
  z-index: 1;
}

.signup-box>p{
  font-size:20px
}
.img-box{
  margin-left:15%
}
.img-btn{
  margin-top:10%;
  margin-left:5%;
  height:10%
}

.input-style{
  width:70%;
  height: 45px;
  border-radius: 4px;
  border:0;
  padding-left:10px;
  opacity: 0.4;
  font-weight: bold;
}

#file-input{
  margin-top:10%;
  margin-left:5%;
  height:10%
}
input::placeholder{
  color: black;
  font-weight: bold;
  /* opacity: .8; */
}
.signup-btn{
  margin-top:10px;
  width:70%;
  height: 45px;
  background-color: #263859 !important;
  border:0;

}

.box {
    width: 80px;
    height: 80px; 
    border-radius: 30%;
    overflow: hidden;
}
.profile {
    width: 100%;
    height: 100%;
    object-fit: cover;
}


</style>

