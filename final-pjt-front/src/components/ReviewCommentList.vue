<template>
  <div class="comment-item my-3">
    <ReviewCommentListItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    class="my-2"
    />
  </div>
</template>

<script>
import ReviewCommentListItem from '@/components/ReviewCommentListItem'
export default {
    name:'ReviewCommentList',
    props:{
      comments:Array
    },
    components:{
      ReviewCommentListItem
    }
}
</script>

<style scoped>


</style>