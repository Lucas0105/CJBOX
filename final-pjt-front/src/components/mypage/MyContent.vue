<template>
  <div class="my-list mx-auto">
    <div class="list-box">
      <b-card class="list-card" no-body>
        <b-tabs pills card >
          <b-tab  title="My List" active>
          <b-card-text class="d-flex flex-column">
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
        </b-tabs>
      </b-card>
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

.list-card{
  width:100%;
  height: 100%;
  background-color: rgba(0,0,0,0.2);
  color: aliceblue;
  overflow-block: auto;
}
.tab-content{
  width:100%;
  height: 100% !important;
}
.card-body{
  padding-bottom:0;
  height: 100%;
}

ul{
  justify-content: center;

}
.tab-content {
  display: flex;
}

.tab-content > .tab-pane {
  display: block; /* undo "display: none;" */
  visibility: hidden;
  margin-right: -100%;
  width: 100%;
}

.tab-content > .active {
  visibility: visible;
}

</style>