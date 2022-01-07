export const getById = (state) => (missionId) => {
	return state.data.find(mission => mission.id === parseInt(missionId))
}