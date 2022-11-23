<template>
  <div class="my-list mx-auto">
    <!-- <div class="list-box">
      <b-card class="list-card" >
        <b-tabs pills card class="h-100 d-flex flex-column" content-class="mt-3 flex-grow-1">
          <div class="panel panel-default">
            <tabset>
        <b-tab  title="My List" active>
          <b-card-text class="d-flex flex-column ">
            <div class="row" style="height:80%">
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
          </b-card-text></b-tab>
            </tabset>
          </div>
          
          <b-tab title="My Review"><b-card-text>
            <MyReviewList
            v-for="review in reviews.reviews"
            :key="review.id"
            :review="review"
            />
            <div class="overflow-auto">
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
          </b-card-text></b-tab>
          <b-tab title="Following"><b-card-text>
            <MyReviewList
            v-for="review in reviews.reviews"
            :key="review.id"
            :review="review"
            />
            <div class="overflow-auto">
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
          </b-card-text></b-tab>
          <b-tab title="Follower"><b-card-text>
            <MyReviewList
            v-for="review in reviews.reviews"
            :key="review.id"
            :review="review"
            />
            <div class="overflow-auto">
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
          </b-card-text></b-tab>
        </b-tabs>
      </b-card>
    </div> -->
  <div class="tabs-container">
    <b-tabs class="h-100 d-flex flex-column" pills content-class="mt-3 flex-grow-1">
      <b-tab title="My List" active>
        <div class="my-tab-content d-flex flex-column justify-content-between">
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
      </b-tab>
      <b-tab title="My Review" active>
        <div class="my-tab-content d-flex flex-column justify-content-between">
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
      </b-tab>
      <b-tab title="Following" active>
        <div class="my-tab-content d-flex flex-column justify-content-between">
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
      </b-tab>
       <b-tab title="Follower" active>
        <div class="my-tab-content d-flex flex-column justify-content-between">
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
      </b-tab>
    </b-tabs>
</div>
  </div>
</template>

<script>
// import MyReviewList from '../mypage/MyReviewList'
// import MyList from '../mypage/MyList'

export default {
    name:'MyContent',
    components:{
      // MyReviewList,
      // MyList
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

.list-card{
  width:100%;
  height: 100%;
  background-color: rgba(0,0,0,0.2);
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