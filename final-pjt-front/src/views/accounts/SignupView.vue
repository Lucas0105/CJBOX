<template>
  <div class="signp-page ">
      <div class="d-flex flex-column signup-box mx-auto" >
        <p >회원가입</p>
        <input type="text" placeholder="아이디" class="mb-2 mx-auto">
        <input type="text" placeholder="닉네임" class="mb-2 mx-auto">
        <input type="text" placeholder="이메일" class="mb-2 mx-auto">
        <input type="text" placeholder="비밀번호" class="mb-2 mx-auto">
        <input type="text" placeholder="비밀번호 확인" class="mb-2 mx-auto">
        <input type="text" placeholder=" 프로필소개" class="mb-2 mx-auto">
        <div class="d-flex img-box">
          <div class="box" style="border:solid 2px black; background-color:white; opacity:0.5">
            <!-- <img class="profile" src=""> -->
          </div>
          <b-button class="img-btn" variant="dark" size="sm">이미지 선택</b-button>
        </div>

        <b-button class="signup-btn mx-auto">회원가입</b-button>
      </div>
  </div>
</template>

<script>
export default {
    name:'SignupView'
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

input{
  width:70%;
  height: 45px;
  border-radius: 4px;
  border:0;
  padding-left:10px;
  opacity: 0.4;
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

