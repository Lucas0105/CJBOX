<template>
    <div class="row search-list">
        <SearchListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie='movie'
        />
    </div>
</template>

<script>
import SearchListItem from '@/components/SearchListItem'

export default {
    name:'SearchList',
    data(){
        return{

        }
    },
    props:{
        movies:Array
    },
    components:{
        SearchListItem
    }
}
</script>

<style scoped>
.search-list{
    margin-top:4%;
    height: 100%;
}

</style>