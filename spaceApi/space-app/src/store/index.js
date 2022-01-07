import Vue from 'vue'
import Vuex, { Store } from 'vuex'
import missions from './missions'
import astronauts from './astronauts'

Vue.use(Vuex)

const mutations = {}

export default new Store({
	modules: {
		missions,
        astronauts
	},
	mutations,
})