<template>
  <div>
    <ReviewCommentListItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
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

<style>

</style>