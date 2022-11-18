import axios from 'axios'

const URL = 'http://127.0.0.1:8000'
const state = () => {
    return {
      recentMovieData :null,
      popularMovieData :null,
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
      'TV영화',
      '스릴러',
      '전쟁',
      '서부',
      ],
    }
  }
  
  const getters = {
  }
  const mutations = {
    GET_RECENT_MOVIE(state, data){
      console.log(data)
      state.recentMovieData = data
    },
    GET_POPULAR_MOVIE(state,data){
      console.log(data)
      state.popularMovieData = data
    }
  }
  const actions = {
    getRecentMovie(context) {
      axios({
        method:'get',
        url:`${URL}/movies/newMovie/1/`
      })
      .then((res)=>{
        context.commit('GET_RECENT_MOVIE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getPopularMovie(context){
      axios({
        meethod:'get',
        url:`${URL}/movies/popular/`
      })
      .then((res)=>{
        context.commit('GET_POPULAR_MOVIE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
  
  export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions,
  }
  