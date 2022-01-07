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
		loadingastronauts: {
			get() {
				return this.$store.state.astronauts.loading
			},
		},
	},
	mounted() {
		this.selectedAstronaut = null
		this.$store.dispatch('astronauts/fetchAstronauts')
	},
}
</script>
