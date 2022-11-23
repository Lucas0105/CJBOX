<template>
  <div class="comment-mask">
    <div class="comment-wrapper d-flex justify-content-center align-items- center">
      <div class="comment-container ">
        <header class="d-flex justify-content-end">
          <b-button class="modal-default-button" @click="$emit('close',reviewId)">
            X
          </b-button>
        </header>
        <body class="body">
          <form @submit.prevent="inputComment" class="d-flex flex-column">
            <input type="text" class="comment-input  mx-auto" maxlength="100" v-model="comment_data">
            <b-button class="comment-btn" type="submit">작성</b-button>
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
      isCommentCreate(){
        return this.$store.getters['user/isCommentCreate']
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
      isCommentCreate : {
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
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border-radius: 10px;
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
  overflow:auto;

}

.comment-input{
  width:80%;
  height: 50px;
  font-size: 1.2em;
}

.comment-btn{
  width:7%
}

.body{
  min-height: 85%;
}
.footer{

}

ul{
  justify-content: center;
}

</style>