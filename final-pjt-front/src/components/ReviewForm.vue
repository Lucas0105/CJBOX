<template>
  <div class="review-list">
    <form @submit.prevent="inputReview" class="review-form" v-if="!isupdate">
      <div v-if="isLogin">

        <h4>나의 관람평</h4>
          <h1 v-if="isLoading">test</h1>
        <div>
          <div class="my-3">
          <star-rating :increment="0.5" v-model="rating"  :show-rating="false" ></star-rating>
          </div>
          
          <label class="d-flex flex-column">
            <textarea name="" id="" cols="10" rows="4"  wrap="hard" maxlength="250" v-model="content" class="mx-auto"></textarea>
            <b-button type="submit" class="t-btn mt-3">등록</b-button>
          </label>
        </div>

      </div>
      <div v-else>
        <p>로그인이 필요한 서비스입니다.
          <router-link :to="{name:'login'}"><span style="color:#FD7013">로그인하러 가기</span></router-link>
        </p>
      </div>
    </form>
    <form v-else @submit.prevent="updateReview">
      <div>
        <h3>
          <h4>나의 관람평 수정</h4>
            <star-rating :increment="0.5" v-model="updaterating" :show-rating="false" ></star-rating>
        </h3>
         <label class="d-flex flex-column">
          <textarea name="" id="" cols="10" rows="4"  wrap="hard" maxlength="250" v-model="updateContent" class="mx-auto"></textarea>
          <b-button type="submit" class="t-btn mt-3">수정</b-button>
        </label>
      </div>
    </form>
    <h1 v-if="isLoading">테스트 중입니다.</h1>
    <ReviewComment
      @close="closeModal"
      v-if="isLoading"
      :reviewId="review.id"
    />
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import ReviewComment from '@/components/ReviewComment'

export default {
    name:'ReviewForm',
    data() {
      return{
        content:null,
        vote:null,
        updateContent:null,
        review_id:null,
        rating: 0,
        updaterating: 0,
        isLoading: false,
      }
    },
    components:{
      StarRating,
      ReviewComment,
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
      },
      reviewLoading(){
        return this.$store.getters['user/isReviewLoading']
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
          this.$store.state.user.reviewLoading = true
          this.content = null
          this.rating = 0
        }

      },
      updateReview(){
        const content = this.updateContent
        const review_id = this.review_id
        const vote = this.updaterating * 2

        const payload ={
          content, review_id, vote
        }
        this.$store.dispatch('user/updateReview', payload)
        this.updateContent = null
        this.updaterating = null
      },
      changeValue(){
      if (this.$store.getters['user/updateReview']){
        this.updateContent = this.$store.getters['user/updateReview'].content
        this.review_id = this.$store.getters['user/updateReview'].id
        this.updaterating = this.$store.getters['user/updateReview'].vote
      }
    },
    changeLoading(){
      this.isLoading = !this.isLoading
    },
    openModal() {
      this.modal = true
    },
    closeModal() {
      this.modal = false
    },
    doSend() {
      if (this.message.length > 0) {
        alert(this.message)
        this.message = ''
        this.closeModal()
      } else {
        alert('메시지를 입력해주세요.')
      }
    }
      
    },
    watch:{
      updateDataChange:{
        handler:'changeValue'
      },
      reviewLoading(){
        
      }
    },
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