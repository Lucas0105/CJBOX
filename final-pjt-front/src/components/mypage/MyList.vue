<template>
  <div class="my-list mx-auto">
    <div class="list-box">
      <b-card class="list-card" no-body>
        <b-tabs pills card>
          
          <b-tab  title="My List" active><b-card-text>
            
          </b-card-text></b-tab>
          <b-tab title="My Review" ><b-card-text>
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
export default {
    name:'MyList',
    components:{
      MyReviewList
    },
    props:{
    },
    data(){
      return{
        currentPage:1,
        perPage:1,
      }
    },
    computed:{
      reviews(){
        return this.$store.state.user.userTotalReview
      }
    },
    methods:{
      getUserTotalReview(){
        this.$store.dispatch('user/getUserTotalReview', this.currentPage)
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
  height: 100%;
  background-color: black;
  color: aliceblue;
}

.card-body{
  padding-bottom:0;
  height: 90%;
}

ul{
  justify-content: center;

}


</style>