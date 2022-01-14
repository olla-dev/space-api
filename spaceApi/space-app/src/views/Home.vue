<template>
  <div class="home">
    <div class="text-center mt-5">
        <h1>Space Mission History</h1>
        <p>verison v0.0.1</p>
        <p>total missions: {{count}}</p>
	</div>
	<div>
		<div class="row">
			<div class="col-3">
				<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
			</div>
			<div class="col-9">
				<PaginationLinks
					v-if="!loadingMissions"
					cls="pagination justify-content-end"
					:current="currentPage"
					:totalPages="totalPages"
					@pagechanged="getMissions" />
			</div>
		</div>
		

		<div class="card mission-card" v-for="m in missions" v-bind:key="m.id">
			<div class="card-header">
				<a :href="m.wikipedia_url" target='_blank'>{{m.name}}</a>
			</div>
			<div class="card-body">
				<div class="row">
					<div class="col-sm-3">
						<img :src="m.photo" v-if="m.photo" />
						<img src="@/assets/rocket.png" v-else />
					</div>
					<div class="col-sm-9">
						<p class="card-text">{{m.brief}}</p>
					</div>
				</div>
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

<style lang="css">
.mission-card {
	margin-bottom: 5px;
}
</style>