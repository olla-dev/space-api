<template>
  <div class="home">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'AstronautList',
  components: {
  },
	computed: {
		astronauts: {
			get() {
				return this.$store.state.astronauts.data
			},
		},
		loadingAstronauts: {
			get() {
				return this.$store.state.astronauts.loading
			},
		},
	},
	mounted() {
		this.getAstronauts(this.currentPage)
	},
	methods: {
		getAstronauts(page = 1) {
			this.selectedAstronaut = null
			this.$store.dispatch('astronauts/fetchAstronauts', {
				page: page
			})
		}
	}
}
</script>
