<template>
  <div class="home">
    <div class="text-center mt-5">
        <h1>Space Mission History</h1>
        <p>verison v0.0.1</p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
	computed: {
		missions: {
			get() {
				return this.$store.state.missions.data
			},
		},
		loadingMissions: {
			get() {
				return this.$store.state.missions.loading
			},
		},
	},
	mounted() {
		this.selectedMission = null
		this.$store.dispatch('missions/fetchMissions')
	},
}
</script>
