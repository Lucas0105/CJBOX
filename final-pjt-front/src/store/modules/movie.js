import axios from 'axios'

const URL = 'http://127.0.0.1:8000'
const state = () => {
    return {
      recentMovieData :null,
      genreMovieData:null,
      movieDetail:null,
      searchResult:null,
      getReview:null,
      similarMovie:null,
      sentiment:null,
      genre_list: [
              '액션',
              '모험',
              '애니메이션',
              '코미디',
              '범죄',
              '다큐멘터리',
              '드라마',
              '가족',
              '판타지',
              '역사',
              '공포',
              '음악',
              '미스터리',
              '로맨스',
              'SF',
              '스릴러',
              '전쟁',
              '서부',
              ],
      detailVideo: null,
      detailCast: null,
    }
  }
  
  const getters = {
    searchResult(state){
      return state.searchResult
    },
    detailMovie(state){
      return state.movieDetail
    },
    getReview(state){
      return state.getReview
    },
    getSimilar(state){
      return state.similarMovie
    },
    getSentiment(state){
      return state.sentiment
    }

    
  }
  const mutations = {
    GET_RECENT_MOVIE(state, data){
      state.recentMovieData = data
    },
    GET_GENRE_MOVIE(state, data){
      state.genreMovieData = data
    },
    GET_MOVIE_DETAIL(state, data){
      console.log(data)
      state.detailCast = data.cast
      state.movieDetail = data.movies
      state.sentiment = data.reviews_avg
      state.detailVideo = data.video
    },
    SEARCH_MOVIE(state, data){
      state.searchResult = data
    },
    RESET_SEARCH(state){
      state.searchResult = null
    },
    GET_REVIEW(state,data){
      console.log(data)
      state.getReview = data
    },
    GET_SIMILAR(state, data){
      state.similarMovie = data
    },   
  }
  const actions = {
    getRecentMovie(context, page) {
      if (!page){
        page = 1
      }
      // console.log(page)
      axios({
        method:'get',
        url:`${URL}/movies/newMovie/${page}/`
      })
      .then((res)=>{
        context.commit('GET_RECENT_MOVIE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getGenreMovie(context, payload){
      let page = payload.genre_page
      let genre_name = payload.genre_name 
      if (!page){
        page = 1
      }
      axios({
        method:'get',
        url:`${URL}/movies/${genre_name}/${page}/`
      })
      .then((res)=>{
        context.commit('GET_GENRE_MOVIE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getMovieDetail(context, movie_id){
      axios({
        method:'get',
        url:`${URL}/movies/detail/${movie_id}/`
      })
      .then((res)=>{
        context.commit('GET_MOVIE_DETAIL', res.data)
        console.log(res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getSimilar(context, id){
      axios({
        method: 'get',
        url:`${URL}/movies/similar/${id}/`
      })
      .then((res) => {
        const movies = res.data.map((movie) => {
          movie.poster_path = 'https://image.tmdb.org/t/p/original'+movie.poster_path
          return movie
        })
        context.commit('GET_SIMILAR', movies)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    searchSubmit(context, title){
      axios({
        method:'get',
        url:`${URL}/movies/search/${title}`
      })
      .then((res)=>{
        context.commit('SEARCH_MOVIE', res.data)
        console.log(res.data)
      })
      .catch((err)=>{
        console.log(err)
        context.commit('SEARCH_MOVIE', '')

      })
    },
    getReviews(context, payload){
      const movie_id = payload.movie_id
      const page = payload.page

      axios({
        method:'get',
        url:`${URL}/reviews/${movie_id}/review/${page}/`
      })
      .then((res)=>{
        console.log(res)
        context.commit('GET_REVIEW', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },


  }
  
  export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions,
  }
  