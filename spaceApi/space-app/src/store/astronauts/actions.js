import { AstronautService, GenericError } from '../../api/astronauts.service'

export async function fetchAstronauts({ commit }) {
	commit('fetchAstronautsRequest')
	try {
		const response = await AstronautService.getAstronauts()
		commit('fetchAstronautsSuccess', response)
		return true
	} catch (e) {
		if (e instanceof GenericError) {
			commit('fetchAstronautsError', { errorCode: e.errorCode, errorMessage: e.message })
		}
		return false
	}
}