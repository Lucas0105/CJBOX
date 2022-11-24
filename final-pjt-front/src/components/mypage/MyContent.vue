<template>
  <div class="my-list mx-auto">
  <div class="tabs-container h-100">
    <b-tabs class="h-100 d-flex flex-column" pills content-class="mt-3 flex-grow-1">
      <b-tab title="My List" active class="h-100">
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
      <b-tab title="My Review" >
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
      <b-tab title="Following" >
        <div class="my-tab-content d-flex flex-column justify-content-between">
            <MyList
              v-for=" movie in myListData.myList"
              :key="movie.id"
              :movie="movie"
              />
            
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
       <b-tab title="Follower" >
        <div class="my-tab-content d-flex flex-column justify-content-between">
            <MyList
              v-for=" movie in myListData.myList"
              :key="movie.id"
              :movie="movie"
              />
            
            <div style="overflow-auto; margin-top:auto">
              <div class="mt-3">
                <b-pagination
                  v-model="currentPage2"
                  pills
                  :total-rows="myListData.page_cnt"
                  :per-page="perPage"
                  first-number
                  @input="getUserTotalReview"
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

export default {
    name:'MyContent',
    components:{
      MyReviewList,
      MyList
    },
    props:{
    },
    data(){
      return{
        currentPage:1,
        perPage:1,
        currentPage2:1,
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