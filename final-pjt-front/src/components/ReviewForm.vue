<template>
  <div class="review-list">
    <form @submit.prevent="inputReview" class="review-form" v-if="!isupdate">
      <div v-if="isLogin">
        <div style="d-flex ">
         <star-rating :increment="0.5" v-model="rating"  :show-rating="false" ></star-rating>
        </div>
        
        <label class="d-flex flex-column">
          <textarea name="" id="" cols="10" rows="4"  wrap="hard" maxlength="250" v-model="content" class="mx-auto"></textarea>
          <b-button type="submit" class="t-btn mt-3">등록</b-button>
        </label>

      </div>
      <div v-else>
        <p>로그인이 필요한 서비스입니다.
          <router-link :to="{name:'login'}">로그인하러 가기</router-link>
        </p>
      </div>
    </form>
    <form v-else @submit.prevent="updateReview">
      <div>
        <h3>
            <h2>Half Stars</h2>
            <star-rating :increment="0.5"></star-rating>
        </h3>
         <label class="d-flex flex-column">
          <textarea name="" id="" cols="10" rows="4"  wrap="hard" maxlength="250" v-model="updateContent" class="mx-auto"></textarea>
          <b-button type="submit" class="t-btn mt-3">등록</b-button>
        </label>
      </div>
    </form>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
    name:'ReviewForm',
    data() {
      return{
        content:null,
        vote:null,
        updateContent:null,
        updateVote:null,
        review_id:null,
        rating: 0,

      }
    },
    components:{
      StarRating
    },
    props:{
      movie:Object
    },
    computed:{
      isLogin(){
        return this.$store.getters['user/isLogin']
      }, 
      isupdate(){
        return this.$store.getters['user/isUpdate']
      },
      updateDataChange(){
        return this.$store.getters['user/updateReview']
      }

    },
    methods:{
      inputReview() {
        const movie_id = this.movie.id
        const content = this.content
        const vote = this.rating * 2
        const payload ={
          movie_id,content,vote
        }
        if (content === null){
          alert('리뷰를 입력해주세요')
        } else if(!vote){
          alert('평점을 입력해 주세요')
        } else{
          this.$store.dispatch('user/inputReview', payload)
          this.content = null
          this.rating = 0
        }

      },
      updateReview(){
        const content = this.updateContent
        const review_id = this.review_id
        const payload ={
          content, review_id
        }
        this.$store.dispatch('user/updateReview', payload)
        this.updateContent = null
      },
        changeValue(){
        if (this.$store.getters['user/updateReview']){
          this.updateContent = this.$store.getters['user/updateReview'].content
          this.review_id = this.$store.getters['user/updateReview'].id
          this.updateVote = this.$store.getters['user/updateReview'].vote
        }
      },
      
    },
    watch:{
      updateDataChange:{
        handler:'changeValue'
      },

    }

}
</script>

<style scoped>
textarea{
  border:none;
  color:aliceblue;
  background-color: #6b778d;
  width:90%;
  resize: none;
  border-radius: 4px;
  font-size:1.2em;
  padding:10px;
}
textarea:focus{
    outline: 0;
}

.review-list{
  text-align: center;
}

.t-btn{
  margin-left:85%;
  width: 10%;
  margin-right:0%;
  background-color: #ff6768;
  border:none;

}
.btn:hover{
  background-color: #6b778d !important;
}

.custom-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;
}

.vue-star-rating{
  justify-content: center;
}
</style>