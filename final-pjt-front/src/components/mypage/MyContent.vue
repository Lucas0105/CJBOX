<template>
  <div class="my-list mx-auto">
  <div class="tabs-container h-100">
    <b-tabs class="h-100 d-flex flex-column" pills content-class="mt-3 flex-grow-1">
      <b-tab title="My List" active class="h-100" @click="defaultPage()">
        <div class="h-100 my-tab-content d-flex flex-column justify-content-between">
            <div class="row h-100 d-flex">
              <MyList
                v-for=" movie in myListData.myList"
                :key="movie.id"
                :movie="movie"
                />
            </div>
            
            <div style="overflow-auto; margin-top:auto">
              <div class="mt-3">
                <b-pagination
                  v-model="currentPage2"
                  pills
                  :total-rows="myListData.page_cnt"
                  :per-page="perPage"
                  first-number
                  @input="getMyList"
                ></b-pagination>
              </div>
        </div>
        </div>
      </b-tab>
      <b-tab title="My Review" @click="defaultPage()">
        <div class="my-tab-content d-flex flex-column justify-content-between">
            <MyReviewList
            v-for="review in reviews.reviews"
            :key="review.id"
            :review="review"
            />
            <div style="overflow-auto; margin-top:auto">
              <div class="mt-3">
                <b-pagination
                  v-model="currentPage"
                  pills
                  :total-rows="reviews.page_cnt"
                  :per-page="perPage"
                  first-number
                  @input="getUserTotalReview"
                ></b-pagination>
              </div>
        </div>
        </div>
      </b-tab>
      <b-tab title="Following" @click="defaultPage()">
        <div class="my-tab-content d-flex flex-column justify-content-between">
          <div class="row h-100 d-flex my-auto ">
            <MyFollowing
              v-for=" following in userFollowing.followings"
              :key="following.id"
              :following="following"
              />
          </div>

            
            <div style="overflow-auto; margin-top:auto">
              <div class="mt-3">
                <b-pagination
                  v-model="currentPage3"
                  pills
                  :total-rows="userFollowing.page_cnt"
                  :per-page="perPage"
                  first-number
                  @input="getMyFollowing"
                ></b-pagination>
              </div>
        </div>
        </div>
      </b-tab>
       <b-tab title="Follower" @click="defaultPage()">
        <div class="my-tab-content d-flex flex-column justify-content-between">
          <div class="row h-100 d-flex my-auto ">
            <MyFollower
              v-for=" follower in userFollower.followers"
              :key="follower.nickname"
              :follower="follower"
              />
          </div>
            <div style="overflow-auto; margin-top:auto">
              <div class="mt-3">
                <b-pagination
                  v-model="currentPage4"
                  pills
                  :total-rows="userFollower.page_cnt"
                  :per-page="perPage"
                  first-number
                  @input="getMyFollower"
                ></b-pagination>
              </div>
        </div>
        </div>
      </b-tab>
    </b-tabs>
</div>
  </div>
</template>

<script>

import MyReviewList from '../mypage/MyReviewList'
import MyList from '../mypage/MyList'
import MyFollowing from '../mypage/MyFollowing'
import MyFollower from '../mypage/MyFollower'


export default {
    name:'MyContent',
    components:{
      MyReviewList,
      MyList,
      MyFollowing,
      MyFollower
    },
    props:{
      userInfo:Object
    },
    data(){
      return{
        perPage:1,
        currentPage:1,
        currentPage2:1,
        currentPage3:1,
        currentPage4:1,
        nickname : this.$route.params.nickname,
        

      }
    },
    computed:{
      reviews(){
        return this.$store.state.user.userTotalReview
      },
      myListData(){
        return this.$store.state.user.mylist
      },
      loginUser(){
        return this.$store.state.user.loginUser.nickname
      },
      userFollower(){
        return this.$store.state.user.userFollower
      },
      userFollowing(){
        return this.$store.state.user.userFollowing
      }
    },
    methods:{
      getUserTotalReview(){
        const nickname =this.nickname
        const page =this.currentPage
        const payload={
          nickname, page
        }
        this.$store.dispatch('user/getUserTotalReview',payload )
      },
      getMyList(){
        const nickname = this.nickname
        const page = this.currentPage2
        
        const payload ={
          nickname, page
        }
        this.$store.dispatch('user/getMyList', payload)
      },
      getMyFollower(){
        const nickname = this.userInfo.user.nickname
        const page = this.currentPage3
        const payload = {
          nickname, page
        }

        this.$store.dispatch('user/getMyFollower', payload)
      },
      getMyFollowing(){
        const nickname = this.userInfo.user.nickname
        const page = this.currentPage3
        const payload = {
          nickname, page
        }
        this.$store.dispatch('user/getMyFollowing', payload)

      },
      defaultPage(){
        this.currentPage =1 
        this.currentPage2 =1 
        this.currentPage3 =1 
        this.currentPage4 =1 
      }
    },
    
    
}
</script>

<style scoped>
.my-list{
  width:70%
}
.list-box{
  width:100%;
  height: 100%;
}

.tabs-container{
  width:100%;
  height: 100%;
  background-color: rgb(0, 0, 0) !important;
  border-radius:10px;
  color: aliceblue;
  overflow-block: auto;
}

.tabs-container {
  height: 100%;
  background: #d8d8d8;
}

.tab-pane {
  height: 100%;
}

.my-tab-content {
  min-height: 100%;
  padding:2%;
}

ul{
  justify-content: center;

}
.card-body{
  height: 100%;
}

.tabs{
  height: 100%;
}


</style>

<style>
.nav-link.active {
  background-color:blueviolet !important;
}

.page-item.active .page-link
{  
    background-color: #ff6768 !important;  
    border-color: #ff6768 !important;  
    color:aliceblue !important;
    box-shadow: none !important;
}
.page-link{
  color: #17223b !important;
}



</style>