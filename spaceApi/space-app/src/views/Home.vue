<template>
  <div class="home">
    <div class="text-center mt-5">
        <h1>Space Mission History</h1>
        <p>verison v0.0.1</p>
        <p>total missions: {{count}}</p>
	</div>
	<div>
		<PaginationLinks
			v-if="!loadingMissions"
			cls="pagination justify-content-end"
			:current="currentPage"
			:totalPages="totalPages"
			@pagechanged="getMissions" />

		<div class="card" v-for="m in missions" v-bind:key="m.id">
			<div class="card-header">
				{{m.name}}
			</div>
			<div class="card-body">
				<img :src="m.photo" />
				<p class="card-text">{{m.brief}}</p>
			</div>
		</div>

		<PaginationLinks
			v-if="!loadingMissions"
			cls="pagination justify-content-end"
			:current="currentPage"
			:totalPages="totalPages"
			@pagechanged="getMissions" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PaginationLinks from '../components/PaginationLinks.vue'

export default {
  name: 'Home',
  components: {
	PaginationLinks
  },
	computed: {
		missions: {
			get() {
				return this.$store.state.missions.data.results
			},
		},
		loadingMissions: {
			get() {
				return this.$store.state.missions.loading
			},
		},
		currentPage: {
			get() {
				return this.$store.state.missions.data.currentPage
			},
		},
		totalPages: {
			get() {
				return this.$store.state.missions.data.totalPages
			},
		},
		count: {
			get() {
				return this.$store.state.missions.data.count
			},
		},
	},
	mounted() {
		this.getMissions(1)
	},
	methods: {
		getMissions(page = 1) {
			this.selectedMission = null
			this.$store.dispatch('missions/fetchMissions', {
				page: page
			})
		},
	}
}
</script>
