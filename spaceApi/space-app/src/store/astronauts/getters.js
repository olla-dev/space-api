export const getById = (state) => (astronautId) => {
	return state.data.find(astronaut => astronaut.id === parseInt(astronautId))
}