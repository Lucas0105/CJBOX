<template>
  <div class="my-page">
    <div class="mypage-wrapper mx-auto  d-flex">
      <TheProfile
      :userInfo = "userInfo"
      />
      <MyContent
      />
    </div>
  </div>
</template>

<script>
import MyContent from '@/components/mypage/MyContent'
import TheProfile from '@/components/mypage/TheProfile'

export default {
    name:'MyPageView',
    components:{
      MyContent,
      TheProfile
    },
    data(){
      return{
        nickname : this.$route.params.nickname,
      }
    },
    computed:{
      userInfo(){
        return this.$store.state.user.userInfo
      },
      changeMyList(){
            return this.$store.getters['user/changingMyList']
        }
    },
    methods:{
      getUserTotalReview(){
        const nickname =this.nickname
        const page = 1
        const payload={
          nickname, page
        }
        this.$store.dispatch('user/getUserTotalReview',payload )
      },
      getUserProfile(){
        this.$store.dispatch('user/getUserProfile', this.nickname)
      },
      getMyList(){
        const nickname = this.nickname
        console.log(nickname)
        const page = 1
        
        const payload ={
          nickname, page
        }
        this.$store.dispatch('user/getMyList', payload)
      }
    },
    created(){
      this.getUserTotalReview()
      this.getUserProfile()
      this.getMyList()
    },
    watch:{
        changeMyList:{
            handler:'getMyList'
        }
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