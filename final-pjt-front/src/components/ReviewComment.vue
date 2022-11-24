<template>
  <div class="comment-mask">
    <div class="comment-wrapper d-flex justify-content-center align-items-center">
      <div class="comment-container ">
        <header class="d-flex justify-content-end">
          <button type="button" class="btn btn-outline-danger" @click="$emit('close',reviewId)">X</button>
        </header>
        <body class="body">
          <form @submit.prevent="inputComment" style="width:100%">
              <div style="width:100%" class="d-flex justify-content-center">
                <input type="text" class="comment-input my-auto" maxlength="100" v-model="comment_data" style="border:none">
                <b-button class="comment-btn my-auto" type="submit" >작성</b-button>
              </div>
          </form>
          <ReviewCommentList
          :comments="comments"
          />
        </body>
        <footer>
          <div class="overflow-auto">
            <div class="mt-3">
              <b-pagination
                v-model="currentPage"
                pills
                :total-rows="pageCnt"
                :per-page="perPage"
                first-number
                @input="getComment"
              ></b-pagination>
            </div>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCommentList from '@/components/ReviewCommentList'

export default {
    name:'ReviewComment',
    data(){
      return{
        comment_data: null,
        currentPage:1,
        perPage:1
      }
    },
    components:{
      ReviewCommentList
    },
    props:{
      reviewId : Number
    },
    computed:{
      comments() {
        return this.$store.getters['user/comments'].comments
      },
      pageCnt() {
        return this.$store.getters['user/comments'].page_cnt
      },
      commentChange(){
        return this.$store.getters['user/commentChange']
      }
    },
    methods:{
      inputComment() {
        const payload ={
          review_id : this.reviewId,
          content : this.comment_data
        }
        this.$store.dispatch('user/inputComment', payload)
        this.comment_data = null
      },
      getComment(){
        console.log(this.currentPage)
        const payload = {
          review_id : this.reviewId,
          page : this.currentPage
        }
        this.$store.dispatch('user/getComment', payload)
      }
    },
    created(){
      this.getComment()
    },
    watch:{
      commentChange : {
        handler : 'getComment'
      }
    }
    
    
}
</script>

<style scoped>

.comment-mask{
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s ease;
  color:black;
}

.comment-wrapper{
  width: 100%;
  height: 100%;
  align-items: center
}

.comment-container{
  width: 70%;
  height: 70%;
  padding: 20px 30px;
  background-color: #263859;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border-radius: 10px;
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
  overflow:auto;
  color:aliceblue
}

.comment-input{
  width:80%;
  height: 50px;
  font-size: 1.2em;
  border-radius: 4px;
}

.comment-btn{
  width:7%;
  background-color: #ff6768;
  border:none;
  height: 50px;
  margin-left: 1%;
}
.comment-btn:hover{
  background-color: #263859;
}
.body{
  min-height: 85%;
  background-color: #263859;

}
.footer{
  background-color: #263859;

}

ul{
  justify-content: center;
}

::-webkit-scrollbar {
  display: none;
}
</style>