<template>
  <div class="login-page">
    <div class="login-box d-flex flex-column mx-auto ">
      <p>로그인</p>
      <input type="text" placeholder="아이디" id="user-id" class="mx-auto mb-3">
      <input type="text" placeholder="비밀번호" id="user-pwd" class="mx-auto mb-3">
      <b-button class="login-btn mx-auto mb-4">로그인</b-button>
      <div class="bottom-box d-flex justify-content-between mx-auto">
        <p>아이디 · 비밀번호 찾기</p>
        <p>회원가입</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'LoginView'
}
</script>

<style scoped>
.login-page{
  /* background-color: #17223b;  */
  position: relative;
  top: -80px;
  background-image : url('@/assets/login-bg.jpg');
  background-repeat: no-repeat;
  height:100vh;
  text-align: center;
  display: flex;
  align-items: center;
  justify-items: center;  
}
.login-box{
  width: 35%;
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
  opacity: .8;
}
input{
  padding-left:10px;
  height:45px;
  border:0;
  border-radius: 4px;

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


</style>