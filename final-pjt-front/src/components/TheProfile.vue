<template>
  <div class="profile-box">
    <h1>profile</h1>
    <div class="d-flex">
      <div class="d-flex img-box">
        <div class="r-box" style="background-color:white;   ">
          <img class="r-profile" :src="userImage" alt="userImg">
        </div>
      </div>
      <div class="content-box">
        <div class="d-flex justify-content-between">
          <p>닉네임</p>
          <div class="d-flex">
            <p>팔로우 0</p>
            <p>팔로잉 0</p>
          </div>
        </div>
        <p>자기소개</p>
        <p>관심 장르</p>
      </div>
    </div>
    <p>프로필 편집</p>
  </div>
</template>

<script>
export default {
    name:'TheProfile'
}
</script>

<style scoped>
.img-box{
  margin:20px
}
.profile-box{
  border:solid 1px blue;  
  min-height: 40%;
}

.r-box{
  width: 150px;
  height: 150px; 
  border-radius: 100%;
  overflow: hidden;
  border:solid 1px red;
}

.r-profile{
  position: relative;
  width: 150px;
  height: 150px;
  border-radius: 50%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.content-box{
  width:80%
}
</style>