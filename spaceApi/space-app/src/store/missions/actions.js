import { MissionService, GenericError } from '../../api/missions.service'

export async function fetchMissions({ commit }) {
	commit('fetchMissionsRequest')
	try {
		const response = await MissionService.getMissions()
		commit('fetchMissionsSuccess', response)
		return true
	} catch (e) {
		if (e instanceof GenericError) {
			commit('fetchMissionsError', { errorCode: e.errorCode, errorMessage: e.message })
		}
		return false
	}
}