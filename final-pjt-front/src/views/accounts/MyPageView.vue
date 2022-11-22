<template>
  <div class="my-page">
    <div class="mypage-wrapper mx-auto  d-flex">
      <TheProfile
      :userInfo = "userInfo"
      />
      <MyList
      />
    </div>
  </div>
</template>

<script>
import MyList from '@/components/mypage/MyList'
import TheProfile from '@/components/mypage/TheProfile'

export default {
    name:'MyPageView',
    components:{
      MyList,
      TheProfile
    },
    data(){
      return{
      }
    },
    computed:{
      userInfo(){
        return this.$store.state.user.userInfo

      }
    },
    methods:{
      getUserTotalReview(){
        this.$store.dispatch('user/getUserTotalReview', 1)
      },
      getUserProfile(){
        const nickname = this.$store.state.user.login_user.nickname
        this.$store.dispatch('user/getUserProfile', nickname)
      }
    },
    created(){
      this.getUserTotalReview()
      this.getUserProfile()
    }
}
</script>

<style scoped>
.my-page{
  position: relative;
  top: -80px;
  height:100vh;
  display: flex;
  background-color: #17223b;
}
.mypage-wrapper{
  width:90%;
  margin-top:100px;
  margin-bottom:1.5%
}
</style>